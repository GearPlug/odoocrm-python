import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='odoocrm-python',
      version='0.1.1',
      description='API wrapper for Odoo CRM written in Python',
      long_description=read('README.md'),
      url='https://github.com/GearPlug/odoocrm-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='GPL',
      packages=['odoocrm'],
      zip_safe=False)
