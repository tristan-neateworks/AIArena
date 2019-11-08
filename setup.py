import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AI-Arena",
    version="0.0.5",
    author="Tristan Neate",
    author_email="tristan@neateworks.com",
    description="AI-Arena beta",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ai-olympics.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
