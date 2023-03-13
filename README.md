# PyFish


[![PyPI](https://img.shields.io/pypi/v/pyfish?color=green)](https://pypi.org/project/pyfish/)
[![Conda](https://img.shields.io/conda/v/bioconda/pyfish?color=green)](https://anaconda.org/bioconda/pyfish)

PyFish is a Python 3 package for creation of [Fish (Muller) plots](https://en.wikipedia.org/wiki/Muller_plot) like the one below.

### Primary features
* polynomial interpolation
* curve smoothing
* high performance
* works with low and high density data

PyFish can be used either as a stand-alone tool or as a plotting library.

<img src="https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/fish.png" width="600" />

## Installation

PyFish requires Python >= 3.8

The package can be installed using Conda (from the bioconda channel)

`conda install -c bioconda pyfish`

or Pip

`pip install pyfish`.



## Input

The program takes two tables:
* one describing the size of individual subgroups at given points in time, referred to as _populations_,
* one describing the parent-child relationships between the subgroups, referred to as _parent tree_.

### Populations

Populations table has the schema `(Id: +int, Step: +int, Pop: +int)`, where:
* `Id` is a numerical identifier of a subgroup`,
* `Step` is a natural ordinal describing the logical time when the population is measured,
* `Pop` is the size of the population of the subgroup at the given step.

An example populations table:

| Id  | Step | Pop |
|-----|------|-----|
| 0   | 0    | 100 |
| 0   | 1    | 40  |
| 0   | 2    | 20  |
| 0   | 3    | 0   |
| 1   | 0    | 10  |
| 1   | 3    | 50  |
| 1   | 5    | 100 |
| 2   | 4    | 20  |
| 2   | 5    | 50  |
| 3   | 0    | 10  |
| 3   | 1    | 20  |
| 3   | 5    | 10  |

### Parent Tree

Parent tree has the schema `(ParentId: +int, ChildId: +int)`, where:
* `ParentId` is an id matching the population table,
* `ChildId` is an id matching the population table describing the direct progeny of the parent.

An example parent tree:

| ParentId | ChildId | 
|----------|---------|
| 0        | 1       |
| 1        | 2       |
| 0        | 3       | 

**Note: there must be exactly one node in the parent tree that has no parent. This is the root (0 in the example above).**


## Tool 

We provide example data. From the root folder of the project call: 

`pyfish tests/populations.csv tests/parent_tree.csv out.png`

This will create a plot called `out.png` in the folder.  

Additional execution parameters are described below.

## Library

The populations and parent_tree tables can be constructed directly as dataframes.

The library contains three public functions:

* `process_data` Takes the input data and parameters and creates data suitable for plotting. 
Additional arguments match the parameters as described below.
* `setup_figure` Resizes the figure and adds labels for axes.  
* `fish_plot` Calls the plotting function on the input parameters.

### Example:
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyfish import fish_plot, process_data, setup_figure

populations = np.array([[0, 0, 100], [0, 1, 40], [0, 2, 20], [0, 3, 0], [1, 0, 10], [1, 3, 50], 
    [1, 5, 100], [2, 4, 20], [2, 5, 50], [3, 0, 10], [3, 1, 20], [3, 5, 10]])
parent_tree = np.array([[0, 1], [1, 2], [0, 3]])
populations_df = pd.DataFrame(populations, columns=["Id", "Step", "Pop"])
parent_tree_df = pd.DataFrame(parent_tree, columns=["ParentId", "ChildId"])
data = process_data(populations_df, parent_tree_df)
setup_figure()
fish_plot(*data)
plt.show()
```

Calling the above code displays the following image:

<img src="https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/test.png" width="350" />

## Parameters

### `-a, --absolute`

Plots absolute population counts at each step.

| Base                          | --absolute                       |
|-------------------------------|----------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/base.png) | ![Absolute plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/abs.png) |

### `-I, --interpolate int`

Fills in missing values by interpolation by a polynomial of the given degree. 
If a value is not given, each population is set to 0 at the first and last step.

| Base                          | --interpolate 2                                |
|-------------------------------|------------------------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/test.png) | ![Interpolated plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/interpolation.png) |

### `-S, --smooth float`

Smoothing of the graph using Gaussian filter. 
The parameter value is the standard deviation of the kernel. 
The bigger the population the bigger the value should be.

**NOTE: If the population values are sparse, using smoothing without interpolation might lead to misleading population sizes.**

| Base                          | --smooth 50                         |
|-------------------------------|-------------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/base.png) | ![Smoothed plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/smooth.png) |

### `-F, --first int+`, `-L, --last int+`

Only limits the steps to the range `[first, last]` inclusive.

| Base                          | --first 4000 --last 4500           |
|-------------------------------|------------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/base.png) | ![Smoothed plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/bound.png) |

### `-M, --cmap string`

Use the specified [matplotlib colormap](https://matplotlib.org/stable/tutorials/colors/colormaps.html). 

Default colormap is rainbow.

| Base                          | --cmap viridis                   |
|-------------------------------|----------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/base.png) | ![Smoothed plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/map.png) |

### `-C, --color_by string`

Color the ids based on a separate column in the populations.csv file.
It will select the first value of the column per id, so the value should be constant for all entries with the same id.

Best combined with a sequential colormap using `--cmap`

| Base                          | --color-by Feature --cmap viridis |
|-------------------------------|-----------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/base.png) | ![Smoothed plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/color_by.png) |


### `-R, --seed int+`

Specifies the seed for the randomization of colors.

| Base                          | --seed 2022                       |
|-------------------------------|-----------------------------------|
| ![Base plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/base.png) | ![Smoothed plot](https://bytebucket.org/schwarzlab/pyfish/raw/main/doc/seed.png) |

### `-W, --width int+`, `-H, --height int+`

Specifies the dimensions for the output image. The size is including the axes' labels.

## Citation
Please cite as: *Adam Streck, Tom L Kaufmann, Roland F Schwarz, SMITH: Spatially Constrained Stochastic Model for Simulation of Intra-Tumour Heterogeneity, Bioinformatics, 2023; https://doi.org/10.1093/bioinformatics/btad102*

## Contact
Email questions, feature requests and bug reports to Adam Streck, `adam.streck@mdc-berlin.de`.

## License
PyFish is available under the MIT License.

## Development
To actively develop the package, we recommend to install pyfish in development mode using pip `pip install -e . --user`.
In order to run the main routine from the command line without installing it first, run `python -m pyfish.main -- tests/populations.csv tests/parent_tree.csv out.png`.

To trigger testing, run `pytest -v .`.
