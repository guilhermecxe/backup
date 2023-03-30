from setuptools import setup, find_packages

setup(
    author="Guilherme Alves",
    description="A package to handle general backup of Python objects using Pickle.",
    name="backup",
    version="0.1.0",
    packages=find_packages(include=["backup"]),
    install_requires=[],
    python_requires='>=3.9',
)