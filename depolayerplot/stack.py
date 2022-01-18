from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
from .layer import Layer

class Stack:
    def __init__(self,x_center,y_base,layers=[Layer()],width=0.4,depth_x=0.08,depth_y=0.08):
        if not isinstance(x_center,float): raise TypeError('x_center must be a float')
        if not isinstance(y_base,float): raise TypeError('y_center must be a float')
        if not hasattr(layers,'__iter__'):
            raise TypeError('layers must be a list or tuple')
        for layer in layers:
            if not isinstance(layer,Layer):
                 raise TypeError('each layer must be a Layer object')
        if not isinstance(width,float): raise TypeError('width must be a float')
        if not isinstance(depth_x,float): raise TypeError('depth_x must be a float')
        if depth_x < 0 : raise TypeError('depth_x must be nonnegative')
        if not isinstance(depth_y,float): raise TypeError('depth_y must be a float')
        if depth_y < 0 : raise TypeError('depth_y must be nonnegative')

        self.x_center = x_center
        self.y_base = y_base
        self.layers = layers
        self.width = width
        self.depth_x = depth_x
        self.depth_y = depth_y

    def add_layer_to_top(self,layer):
        if not isinstance(layer,Layer):
            raise TypeError('layer must be a Layer object')
        self.layers.append(layer)

    def add_layer_to_bottom(self,layer):
        if isinstance(layer,Layer):
            raise TypeError('layer must be a Layer object')
        self.layers.insert(0,layer)
    
    def apply_to_ax(self,ax,render_hidden_faces=False):
        height_from_base = 0
        for layer in self.layers:
            self.__render_layer(ax,layer,height_from_base,render_hidden_faces)
            height_from_base = height_from_base + layer.height
        if not render_hidden_faces:
            height_excluding_top_layer = height_from_base - self.layers[-1].height
            self.__render_top_face(ax,self.layers[-1],height_excluding_top_layer)
            
    def __render_layer(self,ax,layer,height_from_base,render_hidden_faces):
        if render_hidden_faces:
            self.__render_back_face  (ax,layer,height_from_base)
            self.__render_bottom_face(ax,layer,height_from_base)
            self.__render_left_face (ax,layer,height_from_base)
            self.__render_top_face   (ax,layer,height_from_base)
        self.__render_right_face  (ax,layer,height_from_base)
        self.__render_front_face (ax,layer,height_from_base)
        ax.text(self.x_center,self.y_base + height_from_base + layer.height/2,layer.label,
                ha='center',va='center',color=layer.label_color,fontsize=layer.label_size,
                transform=ax.transAxes
        )
        
    def __render_back_face(self,ax,layer,height_from_base):
        x0 = self.x_center - self.width/2 + self.depth_x
        y0 = self.y_base + height_from_base + self.depth_y 
        rect = Rectangle([x0,y0],self.width,layer.height,
                         facecolor=layer.side_face_color,transform=ax.transAxes,
                         edgecolor=layer.edge_color,linewidth=layer.edge_width,
                         joinstyle='round'
        )
        ax.add_patch(rect)

    def __render_bottom_face(self,ax,layer,height_from_base):
        x0 = self.x_center - self.width/2
        x1 = x0 + self.depth_x
        x2 = self.x_center + self.width/2
        x3 = x2 + self.depth_x
        y0 = self.y_base + height_from_base
        y1 = y0 + self.depth_y
        face = Polygon([[x0,y0],[x2,y0],[x3,y1],[x1,y1]],transform=ax.transAxes,
                       facecolor=layer.side_face_color,edgecolor=layer.edge_color,
                       linewidth=layer.edge_width,
                       joinstyle='round'
        )
        ax.add_patch(face)
        
        
    def __render_left_face(self,ax,layer,height_from_base):
        x0 = self.x_center - self.width/2
        x1 = x0 + self.depth_x
        y0 = self.y_base + height_from_base
        y1 = y0 + self.depth_y
        y2 = y0 + layer.height
        y3 = y2 + self.depth_y
        face = Polygon([[x0,y0],[x1,y1],[x1,y3],[x0,y2]],transform=ax.transAxes,
                       facecolor=layer.side_face_color,edgecolor=layer.edge_color,
                       linewidth=layer.edge_width,
                       joinstyle='round')
        ax.add_patch(face)

    def __render_top_face(self,ax,layer,height_from_base):
        x0 = self.x_center - self.width/2
        x1 = x0 + self.depth_x
        x2 = self.x_center + self.width/2
        x3 = x2 + self.depth_x
        y0 = self.y_base + height_from_base + layer.height
        y1 = y0 + self.depth_y
        face = Polygon([[x0,y0],[x2,y0],[x3,y1],[x1,y1]],transform=ax.transAxes,
                       facecolor=layer.side_face_color,edgecolor=layer.edge_color,
                       linewidth=layer.edge_width,
                       joinstyle='round'
        )
        ax.add_patch(face)
    
    def __render_right_face(self,ax,layer,height_from_base):
        x0 = self.x_center + self.width/2
        x1 = x0 + self.depth_x
        y0 = self.y_base + height_from_base
        y1 = y0 + self.depth_y
        y2 = y0 + layer.height
        y3 = y2 + self.depth_y
        face = Polygon([[x0,y0],[x1,y1],[x1,y3],[x0,y2]],transform=ax.transAxes,
                       facecolor=layer.side_face_color,edgecolor=layer.edge_color,
                       linewidth=layer.edge_width,
                       joinstyle='round')
        ax.add_patch(face)

    def __render_front_face(self,ax,layer,height_from_base):
        x0 = self.x_center - self.width/2
        y0 = self.y_base + height_from_base
        rect = Rectangle([x0,y0],self.width,layer.height,transform=ax.transAxes,
                         facecolor=layer.face_color,edgecolor=layer.edge_color,
                         linewidth=layer.edge_width,
                         joinstyle='round')
        ax.add_patch(rect)
