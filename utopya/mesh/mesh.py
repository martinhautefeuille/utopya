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
        __material_map: A dictionary from material index to element index
    """

    def __init__(self, dim):
        """Inits a Mesh class

        Args:
            dim: spatial dimension of the mesh

        Raise:
            ValueError: if dim different from 2 or 3
        """
        if dim not in [2, 3]:
            raise ValueError('Unsupported mesh dim: {}'.format(dim))
        self.__dim = dim
        self.__coord = []
        self.__graph = Graph(dim)
        self.__material_map = {}

    @property
    def dim(self):
        """Getter of spatial dimension"""
        return self.__dim

    @property
    def coord(self):
        """Gets the coordinates"""
        return self.__coord

    @coord.setter
    def coordinates(self, nodes):
        """Sets the coordinates

        Args:
            nodes: a list of nodal coordinates

        Raise:
            ValueError if each coordinate doesn't have the same dim as mesh
        """
        for i, n in enumerate(nodes):
            if len(n) is not self.__dim:
                raise ValueError('Coord {} dim != {}'.format(n, self.__dim))
            self.__coord.append(float(x) for x in n)

    def add_connectivity(self, dim, conn, material=None):
        """Sets the connectivity of mesh entities of dimension dim

        Args:
            dim:      spatial dimension of the mesh entities, which
                      connectivities are given in conn
            conn:     connectivity of mesh entities of spatial dimension dim,
                      given in terms of dim-1 mesh entities
            material: material index

        Raise:
            ValueError if a material index is passed for connectivities of
            spatial dimension strictly lower than the spatial dimension of
            the mesh
        """
        self.__graph.add_boundary(dim, conn)
        if material is not None and dim is not self.__dim:
            raise ValueError(
                    'Material cannot be set for elements of dim {}'.format(dim))
        if material is not None and dim is self.__dim:
            key = int(material)
            # start indexing at the last element index
            conn_len = len(self.__graph.level(dim).boundary)
            conn_range = range(conn_len, len(conn))
            if key not in self.__material_map:
                self.__material_map.update({key: [i for i in conn_range]})
            else:
                self.__material_map[key].append(i for i in conn_range)

#end of file
