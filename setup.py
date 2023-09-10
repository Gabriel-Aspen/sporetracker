from setuptools import setup, find_packages

setup(
    name='sporetracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        "psycopg2-binary"
    ],
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    }
)

