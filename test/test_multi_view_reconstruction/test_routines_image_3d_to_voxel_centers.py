# -*- python -*-
#
#       Copyright 2015 INRIA - CIRAD - INRA
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
# ==============================================================================
import numpy

from openalea.phenomenal.data_structure import(
    Image3D,
    VoxelGrid)

# ==============================================================================


def test_simply_working_1():
    image_3d = Image3D.ones((10, 10, 10),
                            voxels_size=16,
                            dtype=numpy.uint8,
                            world_coordinate=(1, 2, 3))

    vpc = VoxelGrid.from_image_3d(image_3d)

    assert vpc.voxels_position[0] == (1., 2., 3.)
    assert vpc.voxels_position[1] == (1., 2., 19.)
    assert len(vpc.voxels_position) == image_3d.size


def test_simply_working_2():

    image_3d = Image3D.ones((10, 10, 10),
                            voxels_size=16,
                            dtype=numpy.uint8,
                            world_coordinate=(1, 2, 3))

    vpc = VoxelGrid.from_image_3d(image_3d)

    assert vpc.voxels_position[0] == (1., 2., 3.)
    assert vpc.voxels_position[1] == (1., 2., 19.)
    assert len(vpc.voxels_position) == image_3d.size

    im = vpc.to_image_3d()

    assert im.ndim == 3
    assert im.size == len(vpc.voxels_position)
    assert (im == image_3d).all()
    assert image_3d.world_coordinate == (1, 2, 3)


if __name__ == "__main__":
    for func_name in dir():
        if func_name.startswith('test_'):
            print("{func_name}".format(func_name=func_name))
            eval(func_name)()
