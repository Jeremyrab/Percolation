import numpy as np

from DisjointSet import DisjointSet
from Utils import Utils
import itertools
import random
import cv2


class PercolationGenerator:
    def __init__(self, dim):
        """
        Creates a percolation generator
        :param dim: The dimensions in the form of a list
        """
        self.n = len(dim)
        self.dim = dim

    def generate_percolation(self, p):
        # Create the disjointset
        disjoint_set = DisjointSet(self.dim)

        # Create all the products
        dim_range_list = [range(dim) for dim in self.dim]
        dim_products = itertools.product(*dim_range_list)

        # Go through every coordinate
        for product in dim_products:
            explore = np.zeros(self.n, dtype=int)
            # Go through every dimension
            for i, dim in enumerate(product):
                # Shift the -1 to the right
                explore[i], explore[i - 1] = -1, 0
                # Check if place to explore backwards will not cause an index error
                if dim != 0:
                    # See if it connects with probability p
                    if random.random() <= p:
                        new = tuple(np.array(product) + explore)
                        disjoint_set.union(product, new)

        return disjoint_set

    def print_percolation_grid(self, p, filename):
        percolation_set = self.generate_percolation(p)
        colour_key = {}

        if self.n != 2:
            raise Exception("Can only print 2d")

        # Creat the image grid
        grid = np.zeros(self.dim + [3])

        # Create all the products
        dim_range_list = [range(dim) for dim in self.dim]
        dim_products = itertools.product(*dim_range_list)

        # Go through every coordinate
        for product in dim_products:

            # Get the root colour
            root = percolation_set.find(product)

            # If it doesn't exist create the key
            if not colour_key.get(root):
                colour_key[root] = Utils.generate_rgb()

            grid[product] = colour_key[root]

        cv2.imwrite(f"{filename}.png", grid)


a = PercolationGenerator([200,500])
a.print_percolation_grid(0.4)