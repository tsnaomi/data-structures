from setuptools import setup


long_description = (
    'This is a package that provides some basic data structures and ',
    'algorithms implemented in Python.'
    )

setup(
    name='data-structures',  # CHANGE!
    version='0.1-dev',
    long_description=long_description,
    license='MIT',  # include license in docs directory
    packages=['data-structures', ],
    install_requires=['setuptools', ],

    # the project url
    url='http://github.com/tsnaomi/data-structures',  # CHANGE!

    # author details
    author='Naomi Tachikawa Shapiro',
    author_email='naomitshapiro@gmail.com',
    )
