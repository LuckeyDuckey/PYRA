from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PYRA",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pygame-ce"],
    author="LuckeyDuckey",
    description="A small Python package that allows developers to quickly build clean, modern user interfaces in pygame-ce. With simple-to-use components and layouts, PYRA makes UI development in pygame-ce fast, intuitive, and visually appealing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LuckeyDuckey/PYRA",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
