from setuptools import setup, find_packages

setup(
    name='hamster',
    version='1.0.0',
    description='A lightweight Python library for deepfake detection using MesoNet.',
    author='Rooha Tanveer',
    author_email='rooha9tanveer@gmail.com',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.8',
        'opencv-python',
        'numpy'
    ],
    include_package_data=True,
    zip_safe=False
)
