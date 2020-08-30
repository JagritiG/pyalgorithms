"""
setup.py serves two primary functions:
It’s the file where various aspects of your project are configured.
The primary feature of setup.py is that it contains a global setup() function.
The keyword arguments to this function are how specific details of your project are defined.
It’s the command line interface for running various commands that relate to packaging tasks.
To get a listing of available commands, run python setup.py --help-commands.
"""
import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
with open("here/README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyalgorithms",
    version="0.0.1",
    description="An algorithmic data analysis library in python",
    long_description=long_description,
    long_description_content_type="markdown",

    # Author details
    author="Jagriti Goswami",
    author_email="jagritigoswami84@gmail.com",


    # The project's main homepage.
    url="https://github.com/JagritiG/pyalgorithms",

    # Choose your license
    license='MIT',

    packages=setuptools.find_packages(),
    classifiers=[
        # Indicate who your project is intended for
        "Intended Audience :: Software Developer",
        "Topic :: Software Development :: Build Tools",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",

        # Specify the Python versions you support here.
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)

