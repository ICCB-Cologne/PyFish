# PyFish

PyFish is a Python package for creation of [Fish (Muller) plots](https://en.wikipedia.org/wiki/Muller_plot) like this one:

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
| 0   | 3    | 10  |
| 1   | 1    | 10  |
| 1   | 3    | 50  |
| 1   | 5    | 100 |
| 2   | 4    | 0   |
| 2   | 5    | 50  |
| 3   | 0    | 10  |
| 3   | 1    | 10  |
| 3   | 5    | 20  |

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

## Execution
