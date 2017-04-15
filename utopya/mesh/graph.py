#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


from mesh.graph_level import GraphLevel


class Graph:
    """Mesh graph containing dim+1 "graph levels" of boundary and coboundary

    Attributes:
        __dim:    A integer value of the spatial dimension of the mesh
        __levels: A list of graph levels
    """

    def __init__(self, dim):
        """Inits a mesh graph

        Args:
            A spatial dimension of the mesh

        Raise:
            ValueError: if mesh dim different from 2 or 3
        """
        if dim not in [2, 3]:
            raise ValueError('Unsupported mesh dim: {}'.format(dim))
        self.__dim = dim
        self.__levels = [GraphLevel(dim, i) for i in range(dim+1)]

    def add_boundary(self, dim, connectivities):
        """Add connectivity of bondary to all the mesh entities of level dim

        Arg:
            dim:            spatial dimension of the graph level to which
                            boundary connectivities is going to be added
            connectivities: For each mesh entities of the graph level dim,
                            it is the list of dim-1 mesh entities connected.
                                       1
                                 +-----------+
                                 |           |
                                 |           |
                               4 |     A     | 2
                                 |           |
                                 |           |
                                 +-----------+
                                       3
                            e.g. the boundary of face A is the following list
                            of egde ids: [1, 2, 3, 4]

        Raise:
            ValueError: if dim negative of greate than mesh dimension
        """
        if not 0 <= dim <= self.__dim:
            raise ValueError('No graph level of dimension: {}'.format(dim))
        self.__levels[dim].boundary = connectivities

    def level(self, dim):
        """Return the graph level of requested spatial dimension

        Args:
           dim: spatial dimension of the desired graph level

       Raise:
           ValueError: if dim is negative of strictly greater than the spatial
                       dimension of the graph
        """
        if dim not in range(self.__dim+1):
            raise ValueError(
                    'No level of dim {} in graph of dim {}'.format(dim,
                                                                   self.__dim))
        return self.__levels[dim]


# end of file
