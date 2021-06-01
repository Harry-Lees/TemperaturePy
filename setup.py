import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='temperaturePy',
    version='1.0.0',
    description='Simple Temperature conversion library',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/Harry-Lees/TemperaturePy',
    author='Harry Lees',
    author_email='harry.lees@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=['temperature'],
    include_package_data=True,
)