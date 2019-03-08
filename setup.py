from setuptools import setup
import os
version = os.environ['TRAVIS_TAG']

setup(name='my-package', version=version)