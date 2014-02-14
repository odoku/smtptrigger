#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import multiprocessing
import smtpd
import asyncore
from optparse import OptionParser
import ConfigParser
import subprocess
import re
import csv
import datetime


__version__ = '0.0.1'


# =====================================================================
# SMTPTriggerServer
# =====================================================================
class SMTPTriggerServer(smtpd.SMTPServer):
    def __init__(self, config):
        self.patterns = config.patterns
        self.logger = Logger(config.log_filepath)
        smtpd.SMTPServer.__init__(self, (config.server_host, config.server_port), None)
        self.logger.info(
            'Starting SMTP Server ({0}:{1})'.format(config.server_host, config.server_port))

    def destroy(self):
        self.logger.info('Quit SMTP Server.')

    def process_message(self, peer, mailfrom, rcpttos, data):
        for email in rcpttos:
            command = self.resolve(email)
            if command:
                self.logger.info(
                    'From:{0}, To:{1}, Exec:{2}'.format(mailfrom, email, ' '.join(command)))
                worker = Worker(command, data)
                worker.start()
                return worker

    def resolve(self, email):
        for regexp, command in self.patterns:
            if regexp.search(email) is not None:
                return command
        return None


# =====================================================================
# Worker
# =====================================================================
class Worker(multiprocessing.Process):
    def __init__(self, command, data):
        super(Worker, self).__init__()
        self.command = command
        self.data = data
        self.proc = None

    def run(self):
        self.proc = subprocess.Popen(self.command, stdin=subprocess.PIPE)
        return self.proc.communicate(self.data)


# =====================================================================
# Config
# =====================================================================
class AppConfig(dict):
    def _set_default_config(self):
        self.update({
            'server': {
                'host': 'localhost',
                'port': 25,
            },
            'log': {
                'path': '/var/log/smtptrigger.log'
            }
        })

    def __init__(self, file):
        super(AppConfig, self).__init__()
        self._set_default_config()
        self._load_config(file)

    def _get_config_filepath(self, filepath):
        filepathes = [
            filepath,
            '/etc/smtptrigger.conf',
            os.path.join(os.getcwd(), 'smtptrigger.conf'),
        ]

        for filepath in filepathes:
            if filepath and os.path.isfile(filepath):
                return filepath
        return None

    def _load_config(self, file):
        config = ConfigParser.SafeConfigParser()
        if file and hasattr(file, 'read'):
            config.readfp(file)
        else:
            file = self._get_config_filepath(file)
            if not file:
                return
            config.read(file)

        for section in config.sections():
            d = self.setdefault(section, {})
            for key, val in config.items(section):
                d[key] = val

    @property
    def log_filepath(self):
        return self['log']['path']

    @property
    def server_host(self):
        return self['server']['host']

    @property
    def server_port(self):
        return int(self['server']['port'])

    @property
    def triggers(self):
        return dict([(key, val) for key, val in self.items() if key.startswith('trigger:')])

    @property
    def patterns(self):
        patterns = []
        for key, val in self.triggers.items():
            pattern = re.compile(format(val['pattern']))
            command = tuple(csv.reader((val['command'],), delimiter=' '))[0]
            patterns.append((pattern, command))
        return patterns


# =====================================================================
# Logger
# =====================================================================
class Logger(object):
    def __init__(self, filepath=None):
        self.filepath = filepath

    def write(self, level, message):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = u'[{0}][{1}] {2}'.format(now, level, message)
        print line
        if self.filepath:
            with open(self.filepath, 'a') as fp:
                fp.write(line + "\n")

    def info(self, message):
        self.write('info', message)

    def warning(self, message):
        self.write('warning', message)

    def error(self, message):
        self.write('error', message)


# =====================================================================
# Commandline
# =====================================================================
def parse_options(args=None):
    p = OptionParser(version="ver:%s" % __version__)
    p.add_option(
        '-c', '--config', action='store', type='string', default=None, help="Config file.")
    p.add_option(
        '-H', '--host', action='store', type='string', default=None, help="Bind local address.")
    p.add_option(
        '-p', '--port', action='store', type='int', default=None, help="Bind local port.")
    p.add_option(
        '-l', '--log', action='store', type='string', default=None, help="Log filepath.")
    return p.parse_args(args)


def main():
    # Parse options
    options, args = parse_options()

    # Get config
    config = AppConfig(options.config)
    if options.host:
        config['server']['host'] = options.host
    if options.port:
        config['server']['port'] = options.port
    if options.log:
        config['log']['path'] = options.log

    # Create Server
    server = SMTPTriggerServer(config)

    try:
        asyncore.loop()
    except KeyboardInterrupt:
        server.destroy()


if __name__ == '__main__':
    main()
