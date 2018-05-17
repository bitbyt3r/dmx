import sys
from setuptools import setup, find_packages

def read_license():
    with open("LICENSE") as f:
        return f.read()

setup(
    name='dmx485',
    packages=find_packages(),
    version='1.1',
    description='Simple DMX driver using an RS485 adapter',
    long_description="""Simple DMX driver using an RS485 adapter
    """,
    license=read_license(),
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
        'pyserial',
        'numpy',
    ],
)
