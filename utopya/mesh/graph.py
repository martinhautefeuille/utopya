#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


from mesh.graphlevel import GraphLevel


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


# end of file
