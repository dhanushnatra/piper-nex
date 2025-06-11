from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="piper-Nex",
    version="0.1.0",
    description="A Python package for text-to-speech using Piper for simple personal assistant projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="dhanushnatra",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)