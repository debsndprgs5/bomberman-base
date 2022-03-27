import pygame as pg
import constants

GRASS = 0
WATER = 1




textures = {
    GRASS : pg.image.load("image\\grass.png"),
    WATER : pg.image.load("image\\water.png")
    }


tilemap = [
    [GRASS, GRASS, GRASS, WATER],
    [GRASS, GRASS, WATER, GRASS],
    [GRASS, WATER, GRASS, GRASS],
    [WATER, GRASS, GRASS, GRASS]    
    ]



tilesize = 40
mapwidth = len(tilemap.tilemap)
mapheight = len(tilemap.tilemap[0])