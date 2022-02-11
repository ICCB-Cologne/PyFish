import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pyfish",
    version="1.0.0",
    author="Adam Streck, Tom Kaufmann",
    author_email="adam.streck@mdc-berlin.de",
    description="Plotting tool for evolutionary population dynamics. Creates a Fish (Muller) plot.",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license="MIT",
    keywords="plot genomics visualization",
    packages=['pyfish', 'tests'],
    scripts=['pyfish'],
    install_requires=[
        'numpy>=1.14',
        'pandas>=1.0',
        'scipy>=1.0',
        'matplotlib>=3.0'
    ],
)
