from setuptools import setup, find_packages
import os


def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

setup(
    name='ganesha_experimental',
    version='1.0.0',
    author='Elazar Chodjayev',
    author_email='zenmyx@gmail.com',
    packages=find_packages(),
)
