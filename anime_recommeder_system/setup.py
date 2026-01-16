from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "anime recommender",
    version = "0.0.1",
    packages= find_packages(),
    author= "Aditya",
    install_requires= requirements
)