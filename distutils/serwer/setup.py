from distutils.core import setup
setup (
name='Serwer',
version='0.1.0',
author='Waldemar Stal',
author_email = 'waldek_15@o2.pl',
packages=['bib','test'],
scripts=['bin/serv.py','bin/control.py','bin/check.py'],
license='LICENSE.txt',
description='Serwer Game',
long_description = 'README.txt',
install_requires=['python >= 2.7'],
)