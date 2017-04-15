#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


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

    @property
    def boundary(self):
        """Gets the boundary of the graph level"""
        return self.__boundary

    @boundary.setter
    def boundary(self, connec):
        """Sets the boundary of the entities from connectivity connec

        Args:
            connec: for all the mesh entitites in the graph level, list of
                    the dim-1 mesh entitiies that they are connected to.
        """
        # set self.__boundary as a list
        self.__boundary = []
        # then, fill it up
        for e in connec:
            self.__boundary.append([(i, True) for i in e])

    def set_boundary_orientation(self, e, i, isIn):
        """Sets the orientation of dim-1 mesh entity in the boundary of a
            mesh entity

        Args:
            e:    index of a mesh entity in the graph level
            i:    index of a dim-1 mesh entity in the boundary of e
            isIn: True if i is pointing inside e, false otherwise

        Raise:
            TypeError if isIn is not a boolean
        """
        if type(isIn) is not bool:
            raise TypeError('Last argument should be a boolean')
        self.__boundary[e][i][1] = isIn


# end of file
