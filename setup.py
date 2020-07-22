import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_utility",  # Replace with your own username
    version="0.1.0",
    author="Ramtin Abadi",
    author_email="Ramtin.Abadi@gmail.com",
    description="Time utility functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramtinabadi/python-time-utility.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
