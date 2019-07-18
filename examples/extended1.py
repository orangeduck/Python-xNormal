import xNormal
xNormal.path = "C:\\Program Files\\xNormal\\3.19.3\\x64\\xNormal.exe"
xNormal.run("piano_high.obj", "piano_low.obj", "piano.png", width = 256, height = 256, 
                  gen_normals = True, normals_x = "+X", normals_y = "-Z", normals_z = "+Y",
                  gen_ao = True, ao_rays = 64, ao_jitter = True, 
                  gen_convexity = True, convexity_scale = 0.75)