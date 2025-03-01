import pygame

def RenderOutline(RenderSurface, Parameters, CornerRadius):
    OutlineRect = pygame.Rect(
        [0, 0],
        RenderSurface.get_size()
    )
    pygame.draw.rect(
        RenderSurface,
        Parameters.Color,
        OutlineRect,
        border_radius=CornerRadius,
        width=Parameters.Thickness
    )
