import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().replace(  # patch for images
        "./docs/", "https://bitbucket.org/schwarzlab/pyfish/raw/HEAD/docs/"
    )


setup(
    name="pyfish",
    version="1.0.0",
    author="Adam Streck, Tom L. Kaufmann",
    author_email="adam.streck@mdc-berlin.de",
    description="Plotting tool for evolutionary population dynamics. Creates a Fish (Muller) plot.",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license="MIT",
    keywords="plot genomics visualization",
    python_requires='>=3.8',
    packages=['pyfish'],
    entry_points={
        'console_scripts': [
            'pyfish = pyfish.main:main',
        ],
    },
    url="https://bitbucket.org/schwarzlab/pyfish",
    install_requires=[
        'numpy>=1.14',
        'pandas>=1.0',
        'scipy>=1.0',
        'matplotlib>=3.0',
        'pytest>=3.0'
    ],
)
