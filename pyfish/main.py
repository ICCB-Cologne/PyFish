import argparse

import pandas as pd
from matplotlib import pyplot as plt

from pyfish import fish_plot, process_data, setup_figure


def main():
    parser = argparse.ArgumentParser(description='Create a Fish (Muller) plot '
                                                 'for the given evolutionary tree.')
    parser.add_argument("populations", type=str,
                        help="A CSV file with the header \"Id,Step,Pop\".")
    parser.add_argument("parent_tree", type=str,
                        help="A CSV file with the header \"ParentId,ChildId\".")
    parser.add_argument("output", type=str,
                        help="Output image filepath. The format must support alpha channels.")
    parser.add_argument('-a', '--absolute', dest="absolute", action="store_true", default=False,
                        help='Plot the populations in absolute numbers rather than normalized.')
    parser.add_argument("-I", "--interpolation", dest='interpolation', type=int, default=0,
                        help="Order of interpolation for empty data (0 means no interpolation).")
    parser.add_argument("-S", "--smooth", dest="smooth", type=float, default=None,
                        help="STDev for Gaussian convolutional filter. The higher the value "
                             "the smoother the resulting bands will be. Recommended is around 1.0.")
    parser.add_argument("-F", "--first", dest="first_step", type=int,
                        help="The step to start plotting from.")
    parser.add_argument("-L", "--last", dest="last_step", type=int,
                        help="The step to end the plotting at.")
    parser.add_argument("-R", "--seed", dest="seed", type=int,
                        help="Random seed for selection of colors.", default=42)
    parser.add_argument("-M", "--cmap", type=str, default="rainbow",
                        help="Colormap to use. Has to be a matplotlib colormap Uses rainbow by default")
    parser.add_argument("-W", "--width", dest="width", type=int, default=1920,
                        help="Output image width")
    parser.add_argument("-H", "--height", dest="height", type=int, default=1080,
                        help="Output image height")

    # Read
    args = parser.parse_args()
    populations_df = pd.read_csv(args.populations)
    parent_tree_df = pd.read_csv(args.parent_tree)

    # Compute
    data = process_data(populations_df, parent_tree_df, args.first_step, args.last_step,
                        args.interpolation, args.absolute, args.smooth, args.seed, args.cmap)

    # Plot
    setup_figure(args.width, args.height, args.absolute)
    fish_plot(*data)
    plt.savefig(args.output)


if __name__ == '__main__':
    main()

