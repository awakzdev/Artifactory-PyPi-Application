import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

from setuptools import setup


class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="ganesha",
    version="0.0.4",
    author="Elazar Chodjayev",
    author_email="zenmyx@gmail.com@gmail.com",
    description="Packaged .whl python application",
    license="BSD",
    keywords="Assignment project artifact",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['src'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    cmdclass={
        'register': register,
        'upload': upload,
    }
)
