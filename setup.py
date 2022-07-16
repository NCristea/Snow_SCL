# -*- coding: utf-8 -*-

from __future__ import (division,
                        absolute_import,
                        print_function,
                        unicode_literals)

import os
from codecs import open

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# Dependencies.
with open('requirements.txt') as f:
    requirements = f.readlines()
install_requires = [t.strip() for t in requirements]

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hydroplotting',
    version='0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='',
    author_email='',
    maintainer='',
    maintainer_email='',
    python_requires='>=3.8',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering'
    ],
    keywords=[],
    packages=find_packages(),
    install_requires=install_requires,
)