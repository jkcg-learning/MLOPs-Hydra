#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="sai",
    version="0.0.1",
    description="PyTorch Lightning Project Setup",
    author="Jyothish",
    author_email="xxxx",
    url="https://github.com/user/project",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "sai_train = sai.train:main",
            "sai_eval = sai.eval:main",
        ]
    },
)
