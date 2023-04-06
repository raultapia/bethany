from setuptools import setup, find_packages

setup(
    name='bethany',
    author="Raul Tapia",
    author_email="raultapia@us.es",
    license="GPLv3",
    version='1.0.0',
    setup_requires=['setuptools'],
    install_requires=['argparse'],
    packages=find_packages(include=['bethany']),
    entry_points={'console_scripts': ['bethany=bethany.bethany:main']}
)
