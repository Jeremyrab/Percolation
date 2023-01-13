import numpy as np


class DisjointSet:
    def __init__(self, n):
        """
        Creates a disjoint data set in with node indexes being n[0] x n[1] x ... n[m]
        :param n: A list with each element being the dimension
        """
        self.n = len(n)
        self.disjoint_set = -1
        for dim in n[::-1]:
            self.disjoint_set = [self.disjoint_set] * dim
        self.disjoint_set = np.array(self.disjoint_set, dtype=object)

    def find(self, index):
        """
        Finds the root node of a given node index
        :param index: The index of the node in tuple form
        :return: The root node of the given node index
        """
        if type(self.disjoint_set[index]) is not tuple and self.disjoint_set[index] < 0:
            return index
        else:
            root = self.find(self.disjoint_set[index])
            self.disjoint_set[index] = root
            return root

    def union(self, item1, item2):
        """
        Union two nodes together
        :param item1: The index of the first node to be union in tuple form
        :param item2: The index of the second node to be union in tuple form
        :return: A boolean to determine if it was successful or already shared a root
        """
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 == root2:
            return False

        height1 = -self.disjoint_set[root1]
        height2 = -self.disjoint_set[root2]

        if height1 > height2:
            self.disjoint_set[root2] = root1
        elif height1 < height2:
            self.disjoint_set[root1] = root2
        else:
            self.disjoint_set[root1] = root2
            self.disjoint_set[root2] -= 1

        return True