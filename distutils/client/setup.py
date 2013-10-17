from distutils.core import setup
setup (
name='Client',
version='0.1.0',
author='Waldemar Stal',
author_email = 'waldek_15@o2.pl',
packages=['img','bib'],
data_files=['img',['img/gr1.png', 'img/gr2.png', 'img/gr3.png', 'img/mina.png', 'img/plik.jpg']],
scripts=['bin/cl.py'],
license='LICENSE.txt',
description='Client Game',
long_description = 'README.txt',
install_requires=['python >= 2.7'],
)