#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen

import json
from decimal import Decimal
from mesh.mesh import Mesh


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
        print('Could not decode JSON string passed as a stream')
    # get spatial dimension
    dim = meshDict["dim"]
    try:
        mesh = Mesh(dim)
    except ValueError:
        raise ValueError('Unsupported mesh dim: {}'.format(dim))
    # set nodal coordinates
    mesh.coordinates = meshDict["nodes"]
    # set edge connectivity
    mesh.add_connectivity(1, meshDict["edges"])
    # set face connectivity, if 3D
    if dim is 3:
        mesh.add_connectivity(2, meshDict["faces"])
    # set element connectivity
    for s in meshDict["elsets"]:
        mesh.add_connectivity(dim, s["connec"], s["material"])

    # return a populated mesh
    return mesh


# end of file
