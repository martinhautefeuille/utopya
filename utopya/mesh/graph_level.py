#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


from mesh.mesh_entity import MeshEntity

class GraphLevel:
    """Level in the mesh graph containing a boundary and coboundary

    Attributes:
        __meshdim:    An integer value of the spatial dimension of the mesh
        __dim:        An integer value of the spatial dimension of the graph
                      level 
        __boundary:   A list containing all the entities in the level a list of
                      the mesh entities (and whether the mesh entity is facing
                      inward or outward) at the lower level
        __coboundary: A list containing all the entities in the level a list of
                      the mesh entities (and whether the mesh entity is facing
                      inward or outward) at the lower level
    """

    def __init__(self, meshdim, dim):
        """Inits a level of the mesh graph; its boundary and coboundary

        Args:
            meshdim: spatial dimension of the mesh
            dim:     spatial dimension of the graph level

        Raise:
            ValueError: if mesh dim different from 2 or 3
            ValueError: if graph level dim greater than mesh dim
        """
        if meshdim not in [2, 3]:
            raise ValueError('Unsupported mesh dim: {}'.format(meshdim))
        if not 0 <= dim <= meshdim:
            raise ValueError('Unsupported level dim: {}'.format(dim))
        self.__dim = dim
        self.__boundary = None
        self.__coboundary = None

    @boundary.setter
    def boundary(self, connec):
        """Sets the boundary of the entities from connectivity connec

        Args:
            connec: for all the mesh entitites in the graph level, list of
                    the dim-1 mesh entitiies that they are connected to.
        """
        for e in connec:
            self.__boundary.append([MeshEntity(i) for i in e])


# end of file
