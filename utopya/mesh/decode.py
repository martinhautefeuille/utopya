#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen

import json
from decimal import Decimal
from mesh.mesh import Mesh

def make2DMesh(meshDict):
    """Make a 2D mesh from data in dictionary
    """
    return Mesh(meshDict["dim"])


def make3DMesh(meshDict):
    """Make a 3D mesh from data in dictionary
    """
    return Mesh(meshDict["dim"])


def decode(meshStream):
    """Decode JSON mesh data and populate mesh class.

    Args:
        meshStream: JSON stream containing mesh description

    Returns:
        A mesh object

    Raises:
        IOError: could not read file
        JSONDecodeError: mesh file is not a valid JSON document
        ValueError: mesh dim unsupported
    """
    # load full stream into one string 
    meshStr = meshStream.read().replace('\n', '')
    # try to decode JSON string into a dictionary
    try:
        meshDict = json.loads(meshStr, parse_float=Decimal)
    except JSONDecodeError:
        print('Mesh file {} is not a valid JSON document'.format(meshFile))
    if meshDict["dim"] == 3:
        return make3DMesh(meshDict)
    elif meshDict["dim"] == 2:
        return make2DMesh(meshDict)
    else:
        raise ValueError('Mesh file {}: Unsupported mesh dim'.format(meshFile))


# end of file
