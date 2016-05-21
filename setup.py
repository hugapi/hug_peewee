#!/usr/bin/env python
"""Defines the setup instructions for hug_peewee"""
import glob
import os
import subprocess
import sys
from os import path

from setuptools import Extension, find_packages, setup
from setuptools.command.test import test as TestCommand

MYDIR = path.abspath(os.path.dirname(__file__))
JYTHON = 'java' in sys.platform
PYPY = bool(getattr(sys, 'pypy_version_info', False))
CYTHON = False
if not PYPY and not JYTHON:
    try:
        from Cython.Distutils import build_ext
        CYTHON = True
    except ImportError:
        pass

cmdclass = {}
ext_modules = []
if CYTHON:
    def list_modules(dirname):
        filenames = glob.glob(path.join(dirname, '*.py'))

        module_names = []
        for name in filenames:
            module, ext = path.splitext(path.basename(name))
            if module != '__init__':
                module_names.append(module)

        return module_names

    ext_modules = [
        Extension('hug_peewee.' + ext, [path.join('hug_peewee', ext + '.py')])
        for ext in list_modules(path.join(MYDIR, 'hug_peewee'))]
    cmdclass['build_ext'] = build_ext


class PyTest(TestCommand):
    extra_kwargs = {'tests_require': ['pytest', 'mock']}

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


cmdclass['test'] = PyTest

try:
   import pypandoc
   readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError, RuntimeError):
   readme = ''

setup(name='hug_peewee',
      version='0.0.2',
      description='An extension to hug that adds clean integration with the peewee ORM',
      long_description=readme,
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='https://github.com/timothycrosley/hug_peewee',
      license="MIT",
      packages=['hug_peewee'],
      requires=['hug', 'peewee'],
      install_requires=['hug', 'peewee'],
      cmdclass=cmdclass,
      ext_modules=ext_modules,
      keywords='Python, Python3',
      classifiers=['Development Status :: 6 - Mature',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'],
      **PyTest.extra_kwargs)
