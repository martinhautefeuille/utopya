#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


from mesh.graph import Graph


class Mesh:
    """Mesh object containing the graph and the nodal coordinates

    Attributes:
        __dim:   An integer value of the spatial dimension 
        __coord: An array containing the nodal coordinates 
        __graph: A partial representation of the mesh graph
    """

    def __init__(self, dim):
        """Inits a Mesh class

        Args:
            A spatial dimension

        Raise:
            ValueError: if dim different from 2 or 3
        """
        if dim not in [2, 3]:
            raise ValueError('Unsupported mesh dim: {}'.format(dim))
        self.__dim = dim
        self.__coord = []
        self.__graph = Graph(dim)

    @property
    def dim(self):
       """Getter of spatial dimension"""
       return self.__dim


#end of file
