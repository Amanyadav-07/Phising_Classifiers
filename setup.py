# setup.py

from setuptools import setup, find_packages

setup(
    name='phishing_project',  # name of your project
    version='0.1',
    packages=find_packages(),  # automatically find all packages and subpackages
    install_requires=[],       # list any dependencies here
    entry_points={
        'console_scripts': [
            # Example: 'phish = phishing_project.main:main_function'
        ]
    },
)
