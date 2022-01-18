Depolayerplot: Illustrate heterostructures in Matplotlib
========================================================

Depolayerplot is a Python package that visualizes deposition stacks inside Matplotlib Axes. It uses an intuitive and user-friendly object-oriented interface. It produces fully vectorized graphics with highlightable text.

First load package classes: 

.. code-block:: python

    >>> from depolayerplot import Layer, Stack

Then define the deposited layers: 

.. code-block:: python

    >>> substrate = Layer(
    >>>     label = 'sapphire (0001)',
    >>>     face_color = 'aquamarine',
    >>>     height = 0.1
    >>> )
    >>> 
    >>> channel = Layer(
    >>>     label = 'GaN (0001)',
    >>>     face_color = 'tomato',
    >>>     height = 0.05
    >>> )
    >>> 
    >>> dielectric = Layer(
    >>>     label = 'AlN (0001)',
    >>>     face_color = 'palegreen',
    >>>     height = 0.05
    >>> )
    >>> electrode = Layer(
    >>>     label = 'Au (polycrystaline)',
    >>>     face_color = 'gold',
    >>>     height = 0.07
    >>> )
    
Colors must be valid Matplotlib colors. Translucent layers are also supported (via hex codes with an alpha field). Dimensions are in axes fractions.

Then consolidate the layers into a stack object: 

.. code-block:: python

    >>> transistor_stack = Stack(
    >>>     x_center = 0.45,
    >>>     y_base = 0.3,
    >>>     layers = [substrate, channel, dielectric, electrode],
    >>>     width = 0.3
    >>> )

Finally, apply the stack to a Matplotlib axes:

.. code-block:: python

    >>> import matplotlib.pyplot as plt
    >>> figure, axes = plt.subplots()
    >>> transistor_stack.apply_to_ax(axes,render_hidden_faces=False)
    >>> figure.savefig('simple_transistor_stack.pdf',bbox_inches='tight')

.. image:: test/simple_transistor_stack.pdf

Constructor arguments
=====================

``Layer``
---------

.. list-table:: 
    :widths: 1 4
    :header-rows: 1

    * - argument name
      - description
    * - ``label=''``
      - The text written in the center of the front face of the layer. LaTeX and newline characters are all valid. If the text is too large for the layer, it will take up space beyond (both to the right/left and the top/boottom) the layer.
    * - ``height=0.1``
      - The height of the layer, as a fraction of the Matplotlib axes that the stack is applied to.
    * - ``label_color='black'``
      - The color of the label text. Must be a valid Matplotlib color.
    * - ``face_color='white'``
      - The color of the layer's faces. Must be a valid Matplotlib color. Translucent colors are supported via the use of a hex code with an alpha field.
    * - ``side_face_color=None``
      - The color of the side faces (including the top face) of the layer. If set to ``None``, ``face_color`` is used. 
    * - ``label_size='medium'``
      - The font size of the layer label. Matplotlib string sizes (i.e. ``small``, ``x-small``, ``large``, etc.) are valid. Point sizes (i.e. ``10``) are also valid.
    * - ``edge_color='k'``
      - The color of the layer edges . Must be a valid Matplotlib color.
    * - ``edge_width=0.5``
      - The line width of the layer edges. 

|

``Stack``
---------

.. list-table:: 
    :widths: 1 4
    :header-rows: 1

    * - argument name
      - description
    * - ``x_center``
      - The x-position of the graphic in axes fraction. Specifically, it is the position of the center of the front faces.
    * - ``y-base``
      - The y-position of the graphic in axes fraction. Specifically, it is the position of the bottom edge of the bottom-most layer.
    * - ``layers=[Layer()]``
      - A list of the layers, from bottom to top.
    * - ``width=0.4``
      - The width of the front faces, in axes fraction. 
    * - ``depth_x=0.08``
      - The x-span of the depth lines, in axes fraction. Must be greater than 1.
    * - ``depth_y=0.08``
      - The y-span of the depth lines, in axes fraction. Must be greater than 1.

To do: 
======

- Add support for ``depth_x`` and ``depth_y`` arguments that are less than one.
- Add some object that labels one or more layers on either the right or the left (i.e. for repeating heterostructures, or to label the thickness of more than one layer). 