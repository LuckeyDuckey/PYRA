import pygame

import PYRA.Rendering.RenderOutline
import PYRA.Rendering.RenderShadow

def RenderContainer(Parameters):
    # Create surface to render too (plus make it transparent)
    RenderSurface = pygame.Surface(Parameters.Resolution).convert_alpha()
    RenderSurface.fill([0, 0, 0, 0])

    # Render main body
    BodyRect = pygame.Rect(
        [0, 0],
        Parameters.Resolution
    )
    pygame.draw.rect(
        RenderSurface,
        Parameters.Color,
        BodyRect,
        border_radius=Parameters.CornerRadius
    )

    if Parameters.OutlineParameters:
        PYRA.RenderOutline(RenderSurface, Parameters.OutlineParameters, Parameters.CornerRadius)

    if Parameters.ShadowParameters:
        RenderSurface = PYRA.RenderShadow(RenderSurface, Parameters.ShadowParameters, Parameters.CornerRadius)
    
    return RenderSurface
