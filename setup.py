from distutils.core import setup

setup(
    # Application name:
    name="80-20_RULES",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Jay Guzman",
    author_email="j.d.guzman.v@gmail.com",

    # Packages
    packages=["pandas, compose, pip, dill, matplotlib"],

    # Include additional files into the package
    include_package_data=True,

    #
    license="LICENSE.txt",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)
