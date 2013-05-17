SMTP Trigger
===========

This application is an SMTP server which executes a command taking advantage of e-mail reception. 


Options
-------

    --version                     show program's version number and exit
    -h, --help                    show this help message and exit
    -c CONFIG, --config=CONFIG    Config file.
    -H HOST, --host=HOST          Bind local address.
    -p PORT, --port=PORT          Bind local port.
    -l LOG, --log=LOG             Log filepath.
  

Config
------

    [server]
    host = localhost
    port = 20025

    [log]
    path = smtptrigger.log

    [trigger:example]
    pattern = \w+@example.com
    command = python /path/to/script.py
