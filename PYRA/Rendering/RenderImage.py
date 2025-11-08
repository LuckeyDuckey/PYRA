import pygame
from pygame.locals import *

import PYRA.VectorMathClass

def RenderImage(RenderSurface, Parameters):
    ImageSize = PYRA.Vec2(Parameters.Image.get_size())

    # Create new surface for rounding the images corners
    ImageRoundedCorners = pygame.Surface(ImageSize).convert_alpha()
    ImageRoundedCorners.fill([0, 0, 0, 0])

    # Create alpha mask
    BodyRect = pygame.Rect(
        [0, 0],
        ImageSize
    )
    pygame.draw.rect(
        ImageRoundedCorners,
        [255, 255, 255],
        BodyRect,
        border_radius=Parameters.CornerRadius
    )

    # Add image onto the surface removing the corners
    ImageRoundedCorners.blit(Parameters.Image, [0, 0], special_flags=BLEND_RGBA_MULT)

    CenteredPosition = (PYRA.Vec2(RenderSurface.get_size()) - ImageSize) * Parameters.Anchor
    
    RenderSurface.blit(
        ImageRoundedCorners,
        CenteredPosition
    )
