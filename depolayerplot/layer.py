from matplotlib.colors import is_color_like

class Layer:
    def __init__(self,label='',height=0.1,label_color='black',face_color='white',side_face_color='grey',top_face_color='lightgrey',label_size='medium',edge_color='k',edge_width=0.5):
        
        if not isinstance(label,str):
            raise TypeError(str(type(label)) + 'label must be a string')
        if not isinstance(height,float): raise TypeError('height must be float')
        if not is_color_like(label_color): raise TypeError('label_color must be a valid matplotlib color')
        if not is_color_like(face_color): raise TypeError(face_color,'face_color must be a valid matplotlib color')
        if not is_color_like(side_face_color): raise TypeError('side_face_color must be a valid matplotlib color')
        if not is_color_like(edge_color): raise TypeError('edge_color must be a valid matplotlib color')
        # TODO: Find a way to acertain label_size is valid
        
        self.label = label
        self.height = height
        self.label_color = label_color
        self.face_color = face_color
        self.side_face_color = side_face_color
        self.top_face_color = top_face_color
        self.label_size = label_size
        self.edge_color = edge_color
        self.edge_width = edge_width
