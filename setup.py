''' setup module '''

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io, sys
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

# Argument to capture next git tag version from repo
git_version = sys.argv[1]
del sys.argv[1]

def read(*names, **kwargs):
    """
        read
    """
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

setup(
    name='devops',
    version=git_version,
    license='TBD',
    description='',
    author='Varun Charan',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('../src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        'boto3 >= 1.12.37',
        'click >= 7.1.1',
        'click-option-group >= 0.5.0',
        'pip >= 20.1.1',
        'requests >= 2.23.0',
        'requests-auth >= 5.1.0',
        'retry >= 0.9.2',
        'colorama >= 0.4.4',
        'Flask == 2.0.2',
        'flask_restful == 0.3.9',
        'itsdangerous == 2.0.1',
        'Jinja2 == 3.0.3',
        'MarkupSafe == 2.0.1',
        'Werkzeug == 2.0.2',
        'gunicorn == 20.1.0',
        'hvac >= 0.2.1',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-runner',
        ]
    },
    entry_points={
        'console_scripts': [
            'devops = devops.cli:cli',
        ]
    },
)
