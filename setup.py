from setuptools import setup, find_packages


setup(
    name='smtptrigger',
    version='0.0.1',
    description='I am SMTP server which executes a command taking advantage of e-mail reception.',
    author='odoku',
    author_email='contact@odoku.net',
    keywords='smtp,command,trigger',
    url='http://odoku.net',
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    smtptrigger = smtptrigger:main
    """,
)
