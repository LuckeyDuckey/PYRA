# PYRA UI Library

[![python 3.8](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/) [![pygame-ce 2.5.2](https://img.shields.io/badge/pygamece-2.5.2-green)](https://www.pygame.org/wiki/about)

PYRA (Pygame Rendering Assistant) is a lightweight UI library built on top of pygame-ce for creating clean, modern user interfaces. It’s designed to simplify UI development by using parameter objects to define element properties, layout, and animations—all while keeping your code neat and flexible.

**Note:** This project was originally developed for my own use and isn’t built with usability in mind. I decided to open-source it for anyone interested in experimenting with its features.

![alt text](https://github.com/LuckeyDuckey/PYRA/blob/main/Demo.png)

## Installation

To install the project as a package simply run:

```bash
pip install git+https://github.com/LuckeyDuckey/PYRA.git
```

## Basic Usage

### UI Elements and Parameter Objects

PYRA’s architecture revolves around *UI elements* that are configured using various **Parameter Objects**. These objects let you define the appearance, behavior, and layout of your UI components, the two **Parameter Objects** that come with every element type are:

- **PositionParameters:** Define the position of an element on the screen.
- **ContainerParameters:** Set element size (resolution), background color, corner radius, and shadow properties.

### Creating and Updating Elements

Each UI element is created by passing in the appropriate parameter objects. For example, creating a button element might look like this:

```python
Button = PYRA.ButtonElement(
    PositionParameters = PYRA.PositionParameters(
        Position = PYRA.Vec2([50, 50]),
    ),
    ContainerParameters = PYRA.ContainerParameters(
        Resolution = PYRA.Vec2([100, 50]),
        Color = [255, 255, 255],
    ),
    ButtonParameters = PYRA.ButtonParameters(
        Callback = lambda: print("Button Clicked!"),
    ),
)
```

Once an element is instantiated, you can update its parameters (e.g., position, color) by modifying its parameter objects and re-rendering the UI.

### Containers and Child Elements

A core concept in PYRA is the **ContainerElement**, which acts as a parent for grouping multiple UI elements. Containers handle layout management and positioning of their child elements through the following:

- **ChildElements:** An array of UI elements (buttons, text inputs, etc.) that are contained within the container.
- **Layout Properties:** Set the layout direction (horizontal or vertical), padding, and spacing to control how child elements are arranged.
- **Position Calculation:** After adding child elements, call the `CalculateChildPositions()` method on the container to automatically determine their positions based on the defined layout parameters.

For instance, a container with a horizontal layout might be set up like this:

```python
Container = PYRA.ContainerElement(
    PositionParameters=PYRA.PositionParameters(
        Position=PYRA.Vec2([50, 50]),
    ),
    ContainerParameters=PYRA.ContainerParameters(
        Resolution=PYRA.Vec2([250, 250]),
        Color=[255, 255, 255],
    ),
    ChildElementsParameters=PYRA.ChildElementsParameters(
        ChildElements=[
            # Add your UI elements (e.g., buttons, icons) here
        ],
        Direction="Horizontal",
        Padding=[15, 15, 15, 15],
    ),
)
Container.CalculateChildPositions()
```

## Demo Script

A comprehensive example script is included in the repository. It demonstrates how to assemble various UI elements—including navigation bars, text containers, and input fields—using PYRA’s parameter objects and containers. Check out the `Examples/Basic.py` file for a complete walkthrough.

## Disclaimer

This project was originally created for my personal use and will be expanded over time as I incorporate it into more of my projects, adding features as needed. However, since it was designed specifically for me, the documentation may be lacking, and the overall usability might not be the most intuitive.  

If you're unsure about how something works, I recommend checking the source code or referring to the built-in docstrings. You can view them directly in the source files or by using Python’s `help()` function (e.g., `help(function_name)` or `help(ClassName)`).  

That said, if you're interested in improving PYRA, contributions and feedback are always welcome!

## Contributing

Feel free to fork the repository, submit pull requests, or open issues for bug reports and feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
