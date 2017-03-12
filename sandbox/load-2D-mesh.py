#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


import io
from mesh.mesh import Mesh
from mesh.decode import decode


def main():
    meshStream = io.StringIO("""\
            {
                "dim": 2,
                "nodes": [
                    [ 1.2141200304 ,  0            ],
                    [ 0.37518501282,  1.1547000408 ],
                    [-0.98224699497,  0.71364402771],
                    [-0.98224699497, -0.71364402771],
                    [ 0.37518501282, -1.1547000408 ]
                ],
                "edges": [
                    [ 0, 1],
                    [ 1, 2],
                    [ 2, 3],
                    [ 3, 4],
                    [ 4, 0]
                ],
                "elsets": [{
                "material": 1,
                "connec": [
                    [ 0, 1, 2, 3, 4]
                ]
                }]
            }
            """)
    m = decode(meshStream)
    print('Decoded a mesh of dimension: {}'.format(m.dim))



if __name__ == "__main__":
    main()


# end of file
