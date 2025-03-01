import pygame, PYRA, math, time, sys, random, os
from pygame.locals import *
import numpy as np

pygame.init()
pygame.display.set_caption("PYRA Basic Demo")

Resolution = [780, 488]
Display = pygame.display.set_mode(Resolution, 0, 32)

Clock, FPS = pygame.time.Clock(), 140
LastTime = time.time()

# Allow keys to repeat and allow for text inputs
pygame.key.set_repeat(500, 33)
pygame.key.start_text_input()

HomeIcon = pygame.image.load(f"{os.getcwd()}/Icons/HomeIcon.png").convert_alpha()
BellIcon = pygame.image.load(f"{os.getcwd()}/Icons/BellIcon.png").convert_alpha()
BinIcon = pygame.image.load(f"{os.getcwd()}/Icons/BinIcon.png").convert_alpha()
CalendarIcon = pygame.image.load(f"{os.getcwd()}/Icons/CalendarIcon.png").convert_alpha()
CameraIcon = pygame.image.load(f"{os.getcwd()}/Icons/CameraIcon.png").convert_alpha()
FolderIcon = pygame.image.load(f"{os.getcwd()}/Icons/FolderIcon.png").convert_alpha()
HeartIcon = pygame.image.load(f"{os.getcwd()}/Icons/HeartIcon.png").convert_alpha()
InfoIcon = pygame.image.load(f"{os.getcwd()}/Icons/InfoIcon.png").convert_alpha()
LocationIcon = pygame.image.load(f"{os.getcwd()}/Icons/LocationIcon.png").convert_alpha()
MailIcon = pygame.image.load(f"{os.getcwd()}/Icons/MailIcon.png").convert_alpha()
ProfileIcon = pygame.image.load(f"{os.getcwd()}/Icons/ProfileIcon.png").convert_alpha()
SettingsIcon = pygame.image.load(f"{os.getcwd()}/Icons/SettingsIcon.png").convert_alpha()

Icons = [HomeIcon, CalendarIcon, InfoIcon, HeartIcon, MailIcon, ProfileIcon, FolderIcon, CameraIcon, LocationIcon, BellIcon, BinIcon, SettingsIcon]

ContainerNavigationBar = PYRA.ContainerElement(
    PositionParameters = PYRA.PositionParameters(
        Position = PYRA.Vec2([15, 15]),
    ),
    ContainerParameters = PYRA.ContainerParameters(
        Resolution = PYRA.Vec2([750, 75]),
        Color = [43, 44, 48],
        CornerRadius = 5,
        ShadowParameters = PYRA.ShadowParameters(
            Size = 20,
            Color = [0, 0, 0],
            Intensity = 50
        ),
    ),
    ChildElementsParameters = PYRA.ChildElementsParameters(
        ChildElements = [
            PYRA.ButtonElement(
                PositionParameters = PYRA.PositionParameters(
                    Margin = [0, 0, 0, 16]
                ),
                ButtonParameters = PYRA.ButtonParameters(
                    Callback = lambda : print("Clicked"),
                ),
                ContainerParameters = PYRA.ContainerParameters(
                    Resolution = PYRA.Vec2(45),
                    CornerRadius = 3,
                ),
                ImageParameters = PYRA.ImageParameters(
                    Image = pygame.transform.smoothscale(Icon, PYRA.Vec2(26)),
                ),
                HoverAnimation = PYRA.HoverAnimation(
                    AnimationParameters = PYRA.AnimationParameters(
                        Duration = 0.15,
                        EasingFunction = lambda Time : 4 * pow(Time, 3) if Time < 0.5 else 1 - pow(-2 * Time + 2, 3) / 2,
                    ),
                    OriginalColor = [255, 255, 255, 0],
                    HoverColor = [255, 255, 255, 20],
                ),
                ClickingAnimation = PYRA.ClickingAnimation(
                    AnimationParameters = PYRA.AnimationParameters(
                        Duration = 0.05,
                        EasingFunction = lambda Time : 4 * pow(Time, 3) if Time < 0.5 else 1 - pow(-2 * Time + 2, 3) / 2,
                    ),
                    OriginalColor = [255, 255, 255, 0],
                    ClickingColor = [255, 255, 255, 35],
                ),
            ) for Icon in Icons
        ],
        Direction = "Horizontal",
        JustifyContent = "Start",
        Padding = [15, 15, 15, 15]
    ),
)

ContainerNavigationBar.CalculateChildPositions()

ContainerText = PYRA.ContainerElement(
    PositionParameters = PYRA.PositionParameters(
        Position = PYRA.Vec2([15, 105]),
    ),
    ContainerParameters = PYRA.ContainerParameters(
        Resolution = PYRA.Vec2([368, 368]),
        Color = [43, 44, 48],
        CornerRadius = 5,
        ShadowParameters = PYRA.ShadowParameters(
            Size = 20,
            Color = [0, 0, 0],
            Intensity = 50
        ),
    ),
    ChildElementsParameters = PYRA.ChildElementsParameters(
        ChildElements = [
            PYRA.TextElement(
                PositionParameters = PYRA.PositionParameters(
                    Margin = [0, 15, 0, 0],
                ),
                ContainerParameters = PYRA.ContainerParameters(
                    Resolution = PYRA.Vec2([150, 20]),
                ),
                TextParameters = PYRA.TextParameters(
                    Text = "Title Text",
                    Font = pygame.font.SysFont("segoeuivariable", 25, bold=True),
                    Color = [255, 255, 255],
                    Anchor = PYRA.Vec2([0, 0.5]),
                ),
            ),
            PYRA.TextElement(
                PositionParameters = PYRA.PositionParameters(
                ),
                ContainerParameters = PYRA.ContainerParameters(
                    Resolution = PYRA.Vec2([278, 350]),
                ),
                TextParameters = PYRA.TextParameters(
                    Text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                    Font = pygame.font.SysFont("segoeuivariable", 15),
                    Color = [255, 255, 255],
                    WrapLength = 278,
                    Anchor = PYRA.Vec2([0, 0]),
                ),
            )
        ],
        Direction = "Vertical",
        JustifyContent = "Start",
        Padding = [45, 45, 45, 45]
    ),
)

ContainerText.CalculateChildPositions()

ContainerInput = PYRA.ContainerElement(
    PositionParameters = PYRA.PositionParameters(
        Position = PYRA.Vec2([398, 105]),
    ),
    ContainerParameters = PYRA.ContainerParameters(
        Resolution = PYRA.Vec2([368, 368]),
        Color = [43, 44, 48],
        CornerRadius = 5,
        ShadowParameters = PYRA.ShadowParameters(
            Size = 20,
            Color = [0, 0, 0],
            Intensity = 50
        ),
    ),
    ChildElementsParameters = PYRA.ChildElementsParameters(
        ChildElements = [
            PYRA.TextInputElement(
                 PositionParameters = PYRA.PositionParameters(
                     Margin = [0, 20, 0, 0],
                 ),
                 ContainerParameters = PYRA.ContainerParameters(
                     Resolution = PYRA.Vec2(278, 53),
                     Color = [55, 55, 60],
                     CornerRadius = 5,
                     ShadowParameters = PYRA.ShadowParameters(
                         Size = 5,
                         Color = [0, 0, 0],
                         Intensity = 25
                     ),
                 ),
                 TextInputParameters = PYRA.TextInputParameters(
                     Callback = lambda UserTextInput : print(UserTextInput),
                     CharacterLength = 17,
                     PreviewText = "Input",
                     Font = pygame.font.SysFont("monospace", 25),
                     TextColor = [255, 255, 255],
                     PreviewTextColor = [100, 100, 100],
                 ),
             ),
            PYRA.TextInputElement(
                 PositionParameters = PYRA.PositionParameters(
                     Margin = [0, 20, 0, 0],
                 ),
                 ContainerParameters = PYRA.ContainerParameters(
                     Resolution = PYRA.Vec2(278, 53),
                     Color = [55, 55, 60],
                     CornerRadius = 5,
                     ShadowParameters = PYRA.ShadowParameters(
                         Size = 5,
                         Color = [0, 0, 0],
                         Intensity = 25
                     ),
                 ),
                 TextInputParameters = PYRA.TextInputParameters(
                     Callback = lambda UserTextInput : print(UserTextInput),
                     CharacterLength = 17,
                     PreviewText = "Input",
                     Font = pygame.font.SysFont("monospace", 25),
                     TextColor = [255, 255, 255],
                     PreviewTextColor = [100, 100, 100],
                 ),
             ),
            PYRA.TextInputElement(
                 PositionParameters = PYRA.PositionParameters(
                     Margin = [0, 20, 0, 0],
                 ),
                 ContainerParameters = PYRA.ContainerParameters(
                     Resolution = PYRA.Vec2(278, 53),
                     Color = [55, 55, 60],
                     CornerRadius = 5,
                     ShadowParameters = PYRA.ShadowParameters(
                         Size = 5,
                         Color = [0, 0, 0],
                         Intensity = 25
                     ),
                 ),
                 TextInputParameters = PYRA.TextInputParameters(
                     Callback = lambda UserTextInput : print(UserTextInput),
                     CharacterLength = 17,
                     PreviewText = "Input",
                     Font = pygame.font.SysFont("monospace", 25),
                     TextColor = [255, 255, 255],
                     PreviewTextColor = [100, 100, 100],
                 ),
             ),
            PYRA.ButtonElement(
                 PositionParameters = PYRA.PositionParameters(
                 ),
                 ContainerParameters = PYRA.ContainerParameters(
                     Resolution = PYRA.Vec2(278, 53),
                     Color = [25, 25, 30],
                     CornerRadius = 5,
                     ShadowParameters = PYRA.ShadowParameters(
                         Size = 5,
                         Color = [0, 0, 0],
                         Intensity = 25
                     ),
                 ),
                 ButtonParameters = PYRA.ButtonParameters(
                     Callback = lambda : print("Clicked"),
                 ),
                 TextParameters = PYRA.TextParameters(
                     Text = "Click Me!",
                    Font = pygame.font.SysFont("segoeuivariable", 25),
                    Color = [255, 255, 255],
                ),
                HoverAnimation = PYRA.HoverAnimation(
                    AnimationParameters = PYRA.AnimationParameters(
                        Duration = 0.15,
                        EasingFunction = lambda Time : 4 * pow(Time, 3) if Time < 0.5 else 1 - pow(-2 * Time + 2, 3) / 2,
                    ),
                    OriginalColor = [25, 25, 30],
                    HoverColor = [35, 35, 40],
                ),
                ClickingAnimation = PYRA.ClickingAnimation(
                    AnimationParameters = PYRA.AnimationParameters(
                        Duration = 0.05,
                        EasingFunction = lambda Time : 4 * pow(Time, 3) if Time < 0.5 else 1 - pow(-2 * Time + 2, 3) / 2,
                    ),
                    OriginalColor = [25, 25, 30],
                    ClickingColor = [40, 40, 45],
                ),
             ),
        ],
        Direction = "Vertical",
        JustifyContent = "Start",
        Padding = [45, 45, 45, 45],
    ),
)

ContainerInput.CalculateChildPositions()

while True:
    
    Clock.tick(FPS)
    DeltaTime = time.time() - LastTime
    LastTime = time.time()
    
    MousePosition = PYRA.Vec2(pygame.mouse.get_pos())
    Events = pygame.event.get()
    PYRA.CursorState = pygame.SYSTEM_CURSOR_ARROW
    
    Display.fill([38, 39, 43])

    ContainerNavigationBar.Render(Display, MousePosition, Events, DeltaTime)
    ContainerText.Render(Display, MousePosition, Events, DeltaTime)
    ContainerInput.Render(Display, MousePosition, Events, DeltaTime)

    pygame.mouse.set_cursor(PYRA.CursorState)
    pygame.display.update()

    for Event in Events:
        
        if Event.type == QUIT:
            pygame.quit()
            sys.exit()
