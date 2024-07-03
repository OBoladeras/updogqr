from setuptools import setup, find_packages

setup(
    name='updogqr',
    version='0.38',
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'updog',
        'netifaces'
    ],
    entry_points={
        'console_scripts': [
            'updogqr=updogqr.__main__:main',
        ],
    },
)
