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
            A spatial dimension of the mesh
            A spatial dimension of the graph level

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


# end of file
