# PyFish

PyFish is a Python package for creation of [Fish (Muller) plots](https://en.wikipedia.org/wiki/Muller_plot).

![Example plot](./docs/fish.png)

### Primary features
* polynomial interpolation
* curve smoothing
* high performance
* works with low and high density data

## Getting Started

The package can be installed using Pip:

```
pip install PyFish
```

## Input

The program takes two tables:
* one describing the size of individual subgroups at given points in time, referred to as _populations_,
* one describing the parent-child relationships between the subgroups, referred to as _parent tree_.

