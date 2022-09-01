
# Proyecto 1 - Graficas por Computadora
# Sara Paguaga 20634

from gl import Renderer, V3
from texture import Texture
from shadersSM import *
from shaders import *


width = 960
height = 540

rend = Renderer(width, height)
rend.dirLight = V3(0,0,-1)

rend.background = Texture("models/background.bmp")
rend.glClearBackground()

# Estrella de Mar - Estatica de escala de grises
rend.active_texture = Texture("models/Starfish/Starfish.bmp")
rend.normal_map = Texture("models/Starfish/Starfish_normal.bmp")
rend.active_shader = staticBnW
rend.glLoadModel("models/Starfish/Starfish.obj",
                 translate = V3(-7, -3.2, -10),
                 scale = V3(1.5,1.5,1.5),
                 rotate = V3(30,0,-10))

# Estrella de Mar - Normal
rend.active_texture = Texture("models/Starfish/Starfish.bmp")
rend.normal_map = Texture("models/Starfish/Starfish_normal.bmp")
rend.active_shader =  normalMap
rend.glLoadModel("models/Starfish/Starfish.obj",
                 translate = V3(-5, -4.2, -10),
                 scale = V3(1.5,1.5,1.5),
                 rotate = V3(30,0,-10))

# Pez Mandarina - HSV Conversion
rend.active_texture = Texture("models/MandarinFish/MandarinFish.bmp")
rend.normal_map = Texture("models/MandarinFish/MandarinFish_normal.bmp")
rend.active_shader = hsv
rend.glLoadModel("models/MandarinFish/MandarinFish.obj",
                 translate = V3(-5-1, -0.8+1, -8),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(0,90,0))

# Pez Mandarina - YIQ Conversion
rend.active_texture = Texture("models/MandarinFish/MandarinFish.bmp")
rend.normal_map = Texture("models/MandarinFish/MandarinFish_normal.bmp")
rend.active_shader = yiq
rend.glLoadModel("models/MandarinFish/MandarinFish.obj",
                 translate = V3(-4, 1.5, -10),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(0,70,0))

# Pez Mandarina - Normal
rend.active_texture = Texture("models/MandarinFish/MandarinFish.bmp")
rend.normal_map = Texture("models/MandarinFish/MandarinFish_normal.bmp")
rend.active_shader = normalMap
rend.glLoadModel("models/MandarinFish/MandarinFish.obj",
                 translate = V3(-1.5-1, -1+0.5, -7),
                 scale = V3(0.3,0.3,0.3),
                 rotate = V3(0,105,0))

# Pez Cirujano - Shader Oompa Loompa Effect
rend.active_texture = Texture("models/SurgeonFish/SurgeonFish.bmp")
rend.normal_map = Texture("models/SurgeonFish/SurgeonFish_normal.bmp")
rend.active_shader = oompaLoompa
rend.glLoadModel("models/SurgeonFish/SurgeonFish.obj",
                 translate = V3(1, 0, -17),
                 scale = V3(4.5, 4.5, 4.5),
                 rotate = V3(0,35,0))

# Caballito de mar - HSV
rend.active_texture = Texture("models/Seahorse/Seahorse.bmp")
rend.normal_map = Texture("models/Seahorse/Seahorse_normal.bmp")
rend.active_shader = hsv
rend.glLoadModel("models/Seahorse/Seahorse.obj",
                 translate = V3(4.5+1, 0, -10),
                 scale = V3(0.1/2,0.1/2,0.1/2),
                 rotate = V3(0,20,0))

# Caballito de mar - Normal
rend.active_texture = Texture("models/Seahorse/Seahorse.bmp")
rend.active_shader = normalMap
rend.glLoadModel("models/Seahorse/Seahorse.obj",
                 translate = V3(7.5+1, 0, -11),
                 scale = V3(0.1/2,0.1/2,0.1/2),
                 rotate = V3(0,20,0))

# Concha con normal - Shader: Normal
rend.active_texture = Texture("models/Scallop/scallop.bmp")
rend.normal_map = Texture("models/Scallop/scallop_normal.bmp")
rend.active_shader = normalMap
rend.glLoadModel("models/Scallop/scallop.obj",
                 translate = V3(2, -3.2, -8),
                 scale = V3(0.25,0.25,0.25),
                 rotate = V3(0,45,0))

# Concha - Shader: Negativo
rend.active_texture = Texture("models/Scallop/scallop.bmp")
rend.normal_map = Texture("models/Scallop/scallop_normal.bmp")
rend.active_shader = negative
rend.glLoadModel("models/Scallop/scallop.obj",
                 translate = V3(4.5, -3.2, -10),
                 scale = V3(0.25,0.25,0.25),
                 rotate = V3(0,0,0))

rend.glFinish("Escene.bmp")