xNormal Wrapper
===============

This is a wrapper for the program xNormal that allows for easy scripting and automation.

It is licensed under BSD

For any issues feel free to contact me at:

`contact@theorangeduck.com`

Basic Usage
-----------

The below generates a normal map and ambient occlusion map for the piano meshes.

```python
import xNormal
xNormal.run("piano_high.obj", "piano_low.obj", "piano.png", 
			  width=256, height=256, gen_normals = True, gen_ao = True)
```

Extended Usage 1
----------------

The belows shows some more features.

First the path is set. By default the wrapper assumes `xNormal.exe` is in the PATH variable.

Secondly it generates a normal map with a switch coordinate system and an AO map with fewer rays and jitter. Finally is generates a convexity map.

For a full list of options have a look in the source code where they are listed and easy to see.

Finally it stores the errorcode of xNormal in case of something being wrong.

```python 
import xNormal
xNormal.path = "C:\\Program Files\\xNormal\\3.19.3\\x64\\xNormal.exe"
err = xNormal.run("piano_high.obj", "piano_low.obj", "piano.png", width = 256, height = 256, 
                   gen_normals = True, normals_x = "+X", normals_y = "-Z", normals_z = "+Y",
                   gen_ao = True, ao_rays = 64, ao_jitter = True, 
                   gen_convexity = True, convexity_scale = 0.75)
```

Extended Usage 2
----------------

Scripting xNormal goes via the form of supplying it with a configuration file. These can be generated and saved for later use.

To build a configuration file `xNormal.config` it must be supplied with a list of high mesh options, a list of low mesh options and a list of generation options.

```python
import xNormal
high_config = xNormal.high_mesh_options("piano_high.obj", scale = 2.0)
low_config = xNormal.low_mesh_options("piano_low.obj", scale = 2.0)
generation_config = xNormal.generation_options("piano.png", gen_normals = True)

config = xNormal.config([high_config], [low_config], generation_config)

f = open("later.xml", 'w')
f.write(config)
f.close()
```



