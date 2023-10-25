from setuptools import setup, find_packages
import os

try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md'), encoding='utf-8') as f:
        readme = f.read()
except Exception:
    readme = ''

setup(
    name='bethany',
    author="Raul Tapia",
    author_email="raultapia@us.es",
    url='https://github.com/raultapia',
    license="GPLv3",
    version='1.0.8',
    description='A command line tool to list all BUG, TODO, HACK, NOTE, and FIXME keywords in your code.',
    long_description=readme,
    long_description_content_type='text/markdown',
    setup_requires=['setuptools'],
    install_requires=['argparse'],
    packages=find_packages(include=['bethany']),
    entry_points={'console_scripts': ['bethany=bethany.bethany:main']}
)
