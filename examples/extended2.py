import xNormal
high_config = xNormal.high_mesh_options("piano_high.obj", scale = 2.0)
low_config = xNormal.low_mesh_options("piano_low.obj", scale = 2.0)
generation_config = xNormal.generation_options("piano.png", gen_normals = True)

config = xNormal.config([high_config], [low_config], generation_config)

f = open("later.xml", 'w')
f.write(config)
f.close()