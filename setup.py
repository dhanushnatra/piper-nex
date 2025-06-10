from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="piper-Nex",
    version="0.1.0",
    description="A Python package for text-to-speech using Piper for simple personal assistant projects.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="dhanushnatra",
    packages=find_packages(),
    requires=requirements,
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)