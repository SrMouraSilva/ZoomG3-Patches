# Copyright 2018 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup


def readme():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, 'README.rst'), encoding='UTF-8') as f:
        return f.read()

setup(
    name='ZoomG3-Pedalboards',
    version='0.2.0',

    url='https://github.com/SrMouraSilva/ZoomG3-Pedalboards',

    author='Paulo Mateus Moura da Silva (SrMouraSilva)',
    author_email='mateus.moura@ppgcc.ifce.edu.br',
    maintainer='Paulo Mateus Moura da Silva (SrMouraSilva)',
    maintainer_email='mateus.moura@ppgcc.ifce.edu.br',

    license="Apache Software License v2",

    packages=[],
    
    package_data={},
    install_requires=[
        'jupyter',
        'pandas',
        'matplotlib',
        'cryptography',
        'scrapy',
        'requests',
        'xmltodict',
        'rarfile'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    platforms='Linux',
)
