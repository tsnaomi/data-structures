from setuptools import setup

long_description = """
This is a package that provides some basic data structures implemented in
Python.
"""

setup(
    name="data-structures",
    version="0.1-dev",
    description="Basic Data Structures",
    long_description=long_description,
    # The project URL.
    url='http://github.com/tsnaomi/data-structures',
    # Author details
    author='<Your Name>',
    author_email='<naomitshapiro@gmail.com',
    # Choose your license
    #   and remember to include the license text in a 'docs' directory.
    # license='MIT',
    packages=['data_structures', ],
    install_requires=['setuptools', ]
)
