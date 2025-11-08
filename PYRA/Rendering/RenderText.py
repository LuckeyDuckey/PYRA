import PYRA.VectorMathClass

def RenderText(RenderSurface, Parameters):
    TextSurface = Parameters.Font.render(
        Parameters.Text,
        True,
        Parameters.Color,
        wraplength=Parameters.WrapLength
    )

    PositionOffsetByAnchor = (PYRA.Vec2(RenderSurface.get_size()) - PYRA.Vec2(TextSurface.get_size())) * Parameters.Anchor
    
    RenderSurface.blit(
        TextSurface,
        PositionOffsetByAnchor
    )
