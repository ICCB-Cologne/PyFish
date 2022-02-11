import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.pyfish.pyfish import process_data, fish_plot


def test_pyfish():
    populations = np.array(
        [[0, 0, 100], [0, 1, 40], [0, 2, 20], [0, 3, 10], [1, 1, 10], [1, 3, 50],
         [1, 5, 100], [2, 4, 0], [2, 5, 50], [3, 0, 10], [3, 1, 10], [3, 5, 20]])

    parent_tree = np.array([[0, 1], [1, 2], [0, 3]])

    populations_df = pd.DataFrame(populations, columns=["Id", "Step", "Pop"])
    parent_tree_df = pd.DataFrame(parent_tree, columns=["ParentId", "ChildId"])

    fish_plot(*process_data(populations_df, parent_tree_df, absolute=True, interpolation=1, smooth=1, seed=42))
    plt.show()


test_pyfish()
