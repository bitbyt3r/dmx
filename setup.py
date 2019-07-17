import sys
from setuptools import setup, find_packages

with open("README.md") as FILE:
    long_description = FILE.read()

setup(
    name='dmx485',
    packages=find_packages(),
    version='1.2',
    description='Simple DMX driver using an RS485 adapter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Mark Murnane',
    author_email='mark@hackafe.net',
    url='https://github.com/bitbyt3r/dmx',
    keywords=[
        'dmx',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'pyserial'
    ],
)
