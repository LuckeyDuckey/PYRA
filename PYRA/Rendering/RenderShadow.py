import pygame

import PYRA.VectorMathClass

def RenderShadow(RenderSurface, Parameters, CornerRadius):
    ShadowSurfaceSize = PYRA.Vec2(RenderSurface.get_size()) + Parameters.Size * 2
    ShadowSurface = pygame.Surface(ShadowSurfaceSize).convert_alpha()
    ShadowSurface.fill([0, 0, 0, 0])

    for LayerCount in range(Parameters.Size):
        LayerAlpha = round(Parameters.Intensity * pow(LayerCount / Parameters.Size, 3))
        
        LayerRect = pygame.Rect(
            [LayerCount] * 2,
            PYRA.Vec2(ShadowSurface.get_size()) - 2 * LayerCount
        )
        pygame.draw.rect(
            ShadowSurface,
            Parameters.Color + [LayerAlpha],
            LayerRect,
            width=2,
            border_radius=CornerRadius + (Parameters.Size - LayerCount)
        )

    ShadowSurface.blit(RenderSurface, [Parameters.Size] * 2)
    return ShadowSurface
