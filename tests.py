#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import StringIO
import unittest

import smtptrigger as sf


rootpath = os.path.dirname(os.path.abspath(__file__))


class TestSMTPTrigger(unittest.TestCase):
    def _load_config(self):
        with open(rootpath + '/testdata/test.conf') as f:
            config = f.read()
        config = config % {
            'test001': os.path.join(rootpath, 'test001'),
            'test002': os.path.join(rootpath, 'test002'),
        }
        return config

    def _load_mail(self):
        with open(rootpath + '/testdata/test.mail') as f:
            mail = f.read()
        return mail

    def setUp(self):
        f = StringIO.StringIO(self._load_config())
        config = sf.AppConfig(f)
        self.server = sf.SMTPTriggerServer(config)

    def tearDown(self):
        filepath = os.path.join(rootpath, 'test001')
        os.remove(filepath)

    def test_execute(self):
        mail = self._load_mail()
        from_email = 'hoge@hoge.com'
        to_email = ('test@test001.com',)

        process = self.server.process_message('peer', from_email, to_email, mail)
        process.join()

if __name__ == '__main__':
    unittest.main()
