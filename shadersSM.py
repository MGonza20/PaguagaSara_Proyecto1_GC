# Proyecto 1 - Graficas por Computadora
# Sara Paguaga 20634

import random
from mathLib import *

def staticColors(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    b, g, r = random.random(), random.random(), random.random()

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def staticBnW(render, **kwargs):
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    color = random.random()/2 + 0.5
    b, g, r = color, color, color

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0
        
def oompaLoompa(render, **kwargs):

    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    color = random.random()/2 + 0.5

    b += intensity * 1
    g += (1 - intensity) * color
    r += (1 - intensity) * color

    if b > 1: b = 1
    if g > 1: g = 1
    if r > 1: r = 1

    if b < 0: b = 0
    if g < 0: g = 0
    if r < 0: r = 0

    return r, g, b

def negative(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        b *= 255
        g *= 255
        r *= 255

        b = 255 - b 
        g = 255 - g
        r = 255 - r

        b /= 255
        g /= 255
        r /= 255

        return r, g, b
    else:
        return 0,0,0

def yiq(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    l = [[0.299, 0.587, 0.114], 
          [0.596, -0.275, -0.321],
          [0.212, -0.523, 0.311]]

    rgb = [[r], [g], [b]]
    yiq = mm(l, rgb)

    if 0 <= (yiq[0][0]) <= 1: y = (yiq[0][0])
    else: y = 0

    if 0 <= (yiq[1][0]) <= 1: i = (yiq[1][0])
    else: i = 0

    if 0 <= (yiq[2][0]) <= 1: q = (yiq[2][0])
    else: q = 0

    if intensity > 0:
        return y, i, q
    else:
        return 0,0,0

def hsv(render, **kwargs):
    # Normal calculada por vertice
    u, v, w = kwargs["baryCoords"]
    b, g, r = kwargs["vColor"]
    tA, tB, tC = kwargs["texCoords"]
    nA, nB, nC = kwargs["normals"]

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        # P = Au + Bv + Cw
        tU = tA[0] * u + tB[0] * v + tC[0] * w
        tV = tA[1] * u + tB[1] * v + tC[1] * w

        texColor = render.active_texture.getColor(tU, tV)

        b *= texColor[2]
        g *= texColor[1]
        r *= texColor[0]

    triangleNormal = [nA[0] * u + nB[0] * v + nC[0] * w,
                     nA[1] * u + nB[1] * v + nC[1] * w,
                     nA[2] * u + nB[2] * v + nC[2] * w]

    negDirLight = [-render.dirLight.x, -render.dirLight.y, -render.dirLight.z]
    intensity = dotProduct(triangleNormal, negDirLight)

    b *= intensity
    g *= intensity
    r *= intensity

    b *= 255
    g *= 255
    r *= 255

    rgb = [r, g, b]
    v = max(rgb)
    s = min(rgb) if (v != 0) else 0

    if (v - min(rgb)) != 0:
        if v == r: 
            h = 60*(g-b)/(v - min(rgb))
        if v == g: 
            h = 120 + 60*(b-r)/(v - min(rgb))
        if v == b: 
            h = 240 + 60*(r-g)/(v - min(rgb))
    else: 
        h = 0

    if h < 0: 
        h += 360

    h /= 255
    s /= 255
    v /= 255

    if h >= 1: h = 1
    if s >= 1: s = 1
    if v >= 1: v = 1

    if intensity > 0:
        return h,s,v
    else:
        return 0,0,0
