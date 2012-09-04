class Arc:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.radius = 0
        self.start_angle = 0
        self.end_angle = 0
        self.startx = 0
        self.starty = 0
        self.endx = 0
        self.endy = 0

    def from_file(self, params):
        self.posx = float(params[1])
        self.posy = float(params[2])
        self.radius = float(params[3])
        self.start_angle = int(params[4])
        self.end_angle = int(params[5])
        self.startx = float(params[6])
        self.starty = float(params[7])
        self.endx = float(params[8])
        self.endy = float(params[9])

    def to_file(self):
        s = ("A {posx} {posy} {radius} {start_angle} {end_angle} {startx} "
             "{starty} {endx} {endy}"
            ).format(posx = self.posx,
                     posy = self.posy,
                     radius = self.radius,
                     start_angle = self.start_angle,
                     end_angle = self.end_angle,
                     startx = self.startx,
                     starty = self.starty,
                     endx = self.endx,
                     endy = self.endy)
        return s

class Circle:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.radius = 0

    def from_file(self, params):
        self.posx = float(params[1])
        self.posy = float(params[2])
        self.radius = float(params[3])

    def to_file(self):
        s = ("C {posx} {posy} {radius}").format(posx = self.posx,
                                                posy = self.posy,
                                                radius = self.radius)

class Polyline:
    def __init__(self):
        self.point_count = 0
        self.points = []

    def from_file(self, params):
        # TODO
        pass

    def to_file(self):
        # TODO
        pass

class Rectangle:
    def __init__(self):
        self.startx = 0
        self.starty = 0
        self.endx = 0
        self.endy = 0

    def from_file(self, params):
        self.startx = float(params[1])
        self.starty = float(params[2])
        self.endx = float(params[3])
        self.endy = float(params[4])

    def to_file(self):
        s = ("S {startx} {starty} {endx} {endy}").format(startx = self.startx,
                                                         starty = self.starty,
                                                         endx = self.endx,
                                                         endy = self.endy)
        return s

class Text:
    def __init__(self):
        self.direction = 900
        self.text_size = 0
        self.text_type = ""
        self.text = ""

    def from_file(self, params):
        self.direction = int(params[1])
        self.text_size = float(params[2])
        self.text_type = params[3]
        self.text = params[4]

    def to_file(self):
        s = ("T {direction} {text_size} {text_type} {text}"
            ).format(direction = self.direction,
                     text_size = self.text_size,
                     text_type = self.text_type,
                     text = self.text)
        return s

class Pin:
    def __init__(self):
        self.name = ""
        self.num = 0
        self.posx = 0
        self.posy = 0
        self.length = 0
        self.direction = ""
        self.name_text_size = 0
        self.num_text_size = 0
        self.electrical_type = ""
        self.pin_type = ""

    def from_file(self, params):
        self.name = params[1]
        self.num = int(params[2])
        self.posx = float(params[3])
        self.posy = float(params[4])
        self.length = float(params[5])
        self.direction = params[6]
        self.name_text_size = float(params[7])
        self.num_text_size = float(params[8])
        self.electrical_type = params[9]
        self.pin_type = params[10]

    def to_file(self):
        s = ("X {name} {num} {posx} {posy} {length} {direction} "
             "{name_text_size} {num_text_size} {electrical_type} {pin_type}"
             ).format(name = self.name,
                      num = self.num,
                      posx = self.posx,
                      posy = self.posy,
                      length = self.length,
                      direction = self.direction,
                      name_text_size = self.name_text_size,
                      num_text_size = self.num_text_size,
                      electrical_type = self.electrical_type,
                      pin_type = self.pin_type)
        return s
