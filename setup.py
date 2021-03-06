import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorchvis",
    version="0.0.2",
    author="Anuj Shah",
    author_email="anujonline645@gmail.com",
    description="A package to visualize CNN in PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anujshah1003/pytorchvis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)