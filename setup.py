#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Maxim Ivakhnenko",
    author_email="makci.97@mail.ru",
    url="https://github.com/makci97/hangman",
    license="MIT",
    packages=[
        "hangman",
    ],
    install_requires=[
        "numpy",
        "sys",
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": ["hangman=hangman.hangman:main"]
    }
)
