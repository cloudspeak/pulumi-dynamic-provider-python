from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_dynamic_provider",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudspeak/pulumi-dynamic-provider-python",
    packages=find_packages(exclude=("example")),
    python_requires=">=3.7",
    install_requires=["pulumi>=1.8.1",],
)
