#!/usr/bin/env python3
"""Setup Simber."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


req_pkgs = [
    'colorama'
]


if __name__ == '__main__':
    setuptools.setup(
        name="simber",
        version="0.2.6",
        author="Deepjyoti Barman",
        author_email="deep.barma30@gmail.com",
        description="Simple, minimal, powerful logging library for Python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/deepjyoti30/simber",
        packages=setuptools.find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        python_requires=">=3",
        install_requires=req_pkgs,
        setup_requires=['setuptools'],
    )
