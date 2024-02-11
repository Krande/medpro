import medpro


def test_mesh():
    fp = medpro.MEDFilePost("./tests/examples/box_with_depl.rmed")
    assert len(fp.params_by_name) == 0
    assert len(fp.meshes_by_name) == 1
    assert "mesh" in fp.meshes_by_name

    mesh = fp.meshes_by_name["mesh"]
    assert mesh.name == "mesh"
    assert "G1" in mesh.group_by_name
    assert mesh.num_nodes == 27
    assert mesh.mesh_dim == 3
    assert mesh.space_dim == 3

    g1 = mesh.get_group_by_name("G1")
    assert list(g1.cell_ids) == [3, 4]
    assert list(g1.cell_numbers) == [52, 53]
    assert list(g1.to_profile().node_ids) == [1, 6, 8, 11, 13, 14, 16, 19, 20, 21, 22, 23, 24, 25, 26]