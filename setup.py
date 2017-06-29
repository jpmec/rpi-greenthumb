"""
Setup for rpi-greenthumb module
"""

from setuptools import setup, find_packages

setup(
    name='rpi-greenthumb',
    version='0.0.0',
    description='Raspberry Pi greenthumb module',
    url='https://github.com/jpmec/rpi-greenthumb',
    author='Joshua Petitt',
    license='MIT',
    packages=find_packages(exclude=['*tests*']),
    zip_safe=False,
    keywords=[
        "raspberry pi"
    ]
)
