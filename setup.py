from setuptools import find_packages
from setuptools import setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="fluidspy",
    version="0.0.3",
    description="Implementation of CFD methods in Python",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="A V Aniketh",
    author_email="adimoolamaniketh@gmail.com",
    url="https://github.com/AVAniketh0905/fluidspy.git",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy>=1.24", "typing>=3.7"],
    extras_require={
        "dev": [
            "twine>=4.0.0",
        ],
    },
    python_requires=">=3.10",
)
