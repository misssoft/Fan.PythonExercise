"""
Setup script
"""
from distutils.core import setup

setup(
    name='assessment',
    version='0.1',
    author='dou',
    author_email='dou@gmail.com',
    url='dou.asssessment.com',
    packages=['assessment'],
    package_dir={'assessment':'src/assessment'},
    package_data={'assessment': ['data/*.csv']},
    )
