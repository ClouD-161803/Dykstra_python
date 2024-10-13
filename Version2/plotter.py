"""
This module provides functions for visualizing the intersection
of half-spaces in 1D and 2D.

NOTE: the plt.show() command is omitted,
so that  extra points can be added on the same plot. Make sure to add
this command after calling plot_half_planes()
Functions:

- plot_2d_space(N, c, X, Y, label, cmap):
    Plots a 2D region defined by the intersection of half-spaces.

- plot_1d_space(N, c, cmap):
    Plots a 1D region (line) defined by the intersection of half-spaces.

- plot_half_spaces_intersection(Nc_pairs):
    Plots the intersection of multiple sets of half-spaces. Each set is defined
    by a pair of N (normals) and c (offsets) such that N*x <= c.
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def plot_2d_space(N: np.ndarray, c: np.ndarray, X: np.ndarray, Y: np.ndarray,
                  label: str, cmap: str) -> None:
    """Plots a 2d region defined by the intersection of half spaces"""
    # Initialize Z to 1 (assuming all points are inside initially)
    Z = np.ones_like(X)

    # This loop checks whether a pair of points X,Y lies within the set of constraints
    # Iterate over each half-plane (one per row of N)
    for i in range(N.shape[0]):
        # Calculate the dot product and compare with the offset
        # - X.ravel() and Y.ravel() flatten the 2D arrays X and Y into 1D arrays;
        # - np.vstack([...]) stacks the flattened X and Y arrays vertically,
        #   creating a 2D array where each row represents a point (x, y) from the grid.
        # - .T transposes the resulting array, so each column now represents a point.
        dot_product = np.dot(np.vstack([X.ravel(), Y.ravel()]).T, N[i])
        # Z will contain 1s for points inside the intersection of all
        # half-planes and 0s for points outside
        Z = np.where(dot_product.reshape(X.shape) > c[i], 0, Z)  # Reshape before comparison

    # Colours
    colourmap = cm.get_cmap(cmap)
    colour = colourmap(0.69) # map colourmap to a single colour

    # Plot the filled contours
    plt.contourf(X, Y, Z, cmap=colourmap, alpha=0.5)

    # Create a dummy plot with the label for the legend
    plt.plot([], [], color=colour, alpha=0.5, label=label)


def plot_1d_space(N: np.ndarray, c: np.ndarray, label: str, cmap: str) -> None:
    """Plots a 1d region (line) defined by the intersection of half spaces"""
    # Colours
    colourmap = cm.get_cmap(cmap)
    colour = colourmap(0.69) # map colourmap to a single colour

    # Check for division by 0
    if N[0, 1] == 0:
        # Vertical line
        plt.axvline(x=c[0] / N[0, 0], linestyle='-', linewidth=2,
                    label='Vertical Line', color=colour)
    elif N[0, 0] == 0:
        # Horizontal line
        plt.axhline(y=c[0] / N[0, 1], linestyle='-', linewidth=2,
                    label='Horizontal Line', color=colour)
    else:
        # General line
        x_line = np.linspace(-3, 3, 100)  # Adjust range as needed
        y_line = (c[0] - N[0, 0] * x_line) / N[0, 1]
        plt.plot(x_line, y_line, linewidth=2, label=label, color=colour)


def plot_half_spaces(Nc_pairs: list) -> None:
    """Plots the intersection of multiple sets of half-spaces defined by Nc_pairs,
    where each pair consists of N (normals) and c (offsets) such that N*x <= c.
    Nc_pairs is of the form [('label'_i, 'cmap_i', N_i, c_i), (...), ...]"""

    fig, ax = plt.subplots()

    # Create a grid of x and y values
    x = np.linspace(-3, 3, 500)  # Adjust range as needed
    y = np.linspace(-3, 3, 500)
    X, Y = np.meshgrid(x, y)

    for label, cmap, N, c in Nc_pairs:
        # Distinguish cases based on the rank of N
        rank = np.linalg.matrix_rank(N)
        # 1d case (line)
        if rank == 1:
            plot_1d_space(N, c, label, cmap)
        # 2d case
        elif rank == 2:
            plot_2d_space(N, c, X, Y, label, cmap)
        # Everything else (ADD 3D CASE AT SOME POINT)
        else:
            raise ValueError("Dimension not supported."
                             "Please provide N and c for 1D or 2D cases.")

    # Set aspect ratio to 'equal'
    ax.set_aspect('equal')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Intersection of Multiple Half-Planes')
    plt.grid(True)

    # Add the legend
    plt.legend()