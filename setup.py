import os
from setuptools import setup, find_packages


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
    python_requires='>=3.8',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=['pyfish'],
    install_requires=[
        'numpy>=1.14',
        'pandas>=1.0',
        'scipy>=1.0',
        'matplotlib>=3.0'
    ],
)
