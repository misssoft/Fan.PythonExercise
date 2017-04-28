"""
Setup script
"""
from distutils.core import setup

setup(
    name='assessment',
    versiion='0.1',
    packages=['assessment'],
    package_dir={'assessment':'src/assessment'},
    package_data={'assessmeng':['data/*.csv']},
    )
    