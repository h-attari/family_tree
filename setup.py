from setuptools import setup


setup(
    name = 'family-tree',
    version = '0.0.1',
    packages = ['family-tree'],
    entry_points = {
        'console_scripts': [
            'family-tree = app.__main__:main'
        ]
    })