import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

dependencies = [
    "numpy",
    "scipy",
    "pandas",
    "matplotlib",
    "sklearn",
    "pyyaml>=5.1",
    "torch",
    "pytorch-lightning",
    "tqdm"
]

setup(
    name="onetrack",
    version="0.0.1",
    description="A simple evaluation tool for particle tracking",
    author="Daniel Murnane & Xiangyang Ju",
    install_requires=dependencies,
    packages=["onetrack"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="Apache License, Version 2.0",
    keywords=[
        "machine learning",
        "MLOps",
        "Pytorch",
        "PytorchLightning",
        "Lightning",
        "pipeline"
    ],
    url="https://github.com/murnanedaniel/onetrack",
)
