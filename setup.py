import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Animal Crossing: New Horizons Creatures List",
        version='1.0',
        author='Stephanie Nguyen',
        author_email="stnguyen2@my.waketech.edu",
        url="https://github.com/stefonii/CSC227",
        description="Final Project",
            long_description="CSC 227.0002 - Final Project",
            long_description_content_type="text/plain",
        packages=setuptools.find_packages(),
        python_requires='>=3.6',
)