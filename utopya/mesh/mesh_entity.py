#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


class MeshEntity:
    """Element of the connectivity of either the boundary or the coboundary of
       a graph level

    Attributes:
        __id: An integer value of the id of the mesh
        __in: A boolean true if the mesh entity is oriented pointing inward
              the mesh entity of which it is part of either the boundary or
              the conoundary.
    """

    def __init__(self, index):
        """Inits a mesh entity with its id and set its orientation inward by
        default

        Args:
            index: the global id of the mesh entity in the mesh
        """
        self.__id = index
        self.__in = true

    @property
    def index(self):
        """Gets the id of the mesh entity"""
        return self.__id

    @property
    def inward(self):
        """Gets whether the mesh entity is pointing inward or outward"""
        return self.__in

    @inward.setter
    def inward(self, point_in):
        """Sets whether the mesh entity is pointing inward or outward

        Args:
            point_in: a boolean, true if the mesh entity points inward, false
                      otherwise

        Raise:
            TypeError is point_in is not a boolean
        """
        if type(point_in) is not bool:
            raise TypeError('Argument of MeshEntity.inward must be a boolean')
        self.__inward = point_in


# end of file
