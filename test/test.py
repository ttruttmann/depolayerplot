#!python3

from depolayerplot import Layer, Stack

substrate = Layer(
    label = 'sapphire (0001)',
    face_color = 'aquamarine',
    height = 0.1
)

channel = Layer(
    label = 'GaN (0001)',
    face_color = 'tomato',
    height = 0.05
)

dielectric = Layer(
    label = 'AlN (0001)',
    face_color = 'palegreen',
    height = 0.05
)
electrode = Layer(
    label = 'Au (polycrystaline)',
    face_color = 'gold',
    height = 0.07
)
    
transistor_stack = Stack(
    x_center = 0.45,
    y_base = 0.3,
    layers = [substrate, channel, dielectric, electrode],
    width = 0.3
)

import matplotlib.pyplot as plt
figure, axes = plt.subplots()
transistor_stack.apply_to_ax(axes,render_hidden_faces=False)
figure.savefig('simple_transistor_stack.pdf',bbox_inches='tight')