from pyki.draw import *

class Component:
    def __init__(self):
        # DEF params
        self.name = ""
        self.reference = ""
        self.text_offset = 0
        self.draw_pinnumber = True
        self.draw_pinname = True
        self.unit_count = 0
        self.units_locked = False
        self.option_flag = ""

        # Reference (F0) params
        self.ref_posx = 0
        self.ref_posy = 0
        self.ref_text_size = 0
        self.ref_text_size = 0
        self.ref_text_orientation = "H"
        self.ref_visible = True
        self.ref_htext_justify = "C"
        self.ref_vtext_justify = "C"

        # Name (F1) params
        self.name_posx = 0
        self.name_posy = 0
        self.name_text_size = 0
        self.name_text_size = 0
        self.name_text_orientation = "H"
        self.name_visible = True
        self.name_htext_justify = "C"
        self.name_vtext_justify = "C"

        # draw objects
        self.arcs = []
        self.circles = []
        self.polylines = []
        self.rectangles = []
        self.texts = []
        self.pins = []

    def from_file(self, file_data):
        for line in file_data:
            # split by spaces to get params
            params = line.strip().split(" ")

            # get the command of the line, ie, the first param
            cmd = params[0]

            # DEF = component definition
            if cmd == "DEF":
                self.name = params[1]
                self.reference = params[2]
                # params[3] is reserved, always 0
                self.text_offset = float(params[4])

                if params[5].upper() == "Y":
                    self.draw_pinnumber = True
                else:
                    self.draw_pinnumber = False

                if params[6].upper() == "Y":
                    self.draw_pinname = True
                else:
                    self.draw_pinname = False

                if params[7].upper() == "L":
                    self.units_locked = True
                else:
                    self.units_locked = False

                self.option_flag = params[8]

            # F0 = reference definition
            if cmd == "F0":
                self.ref_posx = float(params[2])
                self.ref_posy = float(params[3])
                self.ref_text_size = float(params[4])
                self.ref_text_orientation = params[5]

                if params[6].upper() == "V":
                    self.ref_visible = True
                else:
                    self.ref_visible = False

                self.ref_htext_justify = params[7]
                self.ref_vtext_justify = params[8]

            # F1 = name definition
            if cmd == "F1":
                self.name_posx = float(params[2])
                self.name_posy = float(params[3])
                self.name_text_size = float(params[4])
                self.name_text_orientation = params[5]

                if params[6].upper() == "V":
                    self.name_visible = True
                else:
                    self.name_visible = False

                self.name_htext_justify = params[7]
                self.name_vtext_justify = params[8]

            # A = arc definition
            if cmd == "A":
                arc = Arc()
                arc.from_file(params)
                self.arcs.append(arc)

            # C = circle definition
            if cmd == "C":
                circle = Circle()
                circle.from_file(params)
                self.circles.append(circle)

            # P = polyline definition
            if cmd == "P":
                poly = Polyline()
                poly.from_file(params)
                self.polylines.append(poly)

            # S = rectangle definition
            if cmd == "S":
                rect = Rectangle()
                rect.from_file(params)
                self.rectangles.append(rect)

            # T = text definition
            if cmd == "T":
                text = Text()
                text.from_file(params)
                self.texts.append(text)

            # pin definition
            if cmd == "X":
                pin = Pin()
                pin.from_file(params)
                self.pins.append(pin)

    def to_file(self):
        file_data = []
        if self.draw_pinnumber:
            draw_pinnumber_str = "Y"
        else:
            draw_pinnumber_str = "N"

        if self.draw_pinname:
            draw_pinname_str = "Y"
        else:
            draw_pinname_str = "N"

        if self.units_locked:
            units_locked_str = "L"
        else:
            units_locked_str = "F"

        file_data.append(("DEF {name} {reference} 0 {text_offset} "
                          "{draw_pinnumber} {draw_pinname} {unit_count} "
                          "{units_locked} {option_flag}"
                          ).format(name = self.name,
                                   reference = self.reference,
                                   text_offset = self.text_offset,
                                   draw_pinnumber = draw_pinnumber_str,
                                   draw_pinname = draw_pinname_str,
                                   unit_count = self.unit_count,
                                   units_locked = units_locked_str,
                                   option_flag = self.option_flag))

        if self.ref_visible:
            ref_visible_str = "V"
        else:
            ref_visible_str = "I"
        file_data.append(("F0 {reference} {posx} {posy} {text_size} "
                          "{text_orientation} {visible} {htext_justify} "
                          "{vtext_justify}"
                          ).format(reference = self.reference,
                                   posx = self.ref_posx,
                                   posy = self.ref_posy,
                                   text_size = self.ref_text_size,
                                   text_orientation = self.ref_text_orientation,
                                   visible = ref_visible_str,
                                   htext_justify = self.ref_htext_justify,
                                   vtext_justify = self.ref_vtext_justify))

        if self.name_visible:
            name_visible_str = "V"
        else:
            name_visible_str = "I"
        file_data.append(("F1 {name} {posx} {posy} {text_size} "
                          "{text_orientation} {visible} {htext_justify} "
                          "{vtext_justify}"
                          ).format(name = self.name,
                                   posx = self.name_posx,
                                   posy = self.name_posy,
                                   text_size = self.name_text_size,
                                   text_orientation = self.name_text_orientation,
                                   visible = name_visible_str,
                                   htext_justify = self.name_htext_justify,
                                   vtext_justify = self.name_vtext_justify))

        file_data.append("DRAW")
        for arc in self.arcs:
            file_data.append(arc.to_file())

        for circle in self.circles:
            file_data.append(circle.to_file())

        for polyline in self.polylines:
            file_data.append(polyline.to_file())

        for rect in self.rectangles:
            file_data.append(rect.to_file())

        for text in self.texts:
            file_data.append(text.to_file())

        for pin in self.pins:
            file_data.append(pin.to_file())

        file_data.append("ENDDRAW")
        file_data.append("ENDDEF")
        return file_data

    def __str__(self):
        s = "{name} - {reference}\n".format(name = self.name,
                                            reference = self.reference)
        for arc in self.arcs:
            s = s + arc.to_file() + "\n"

        for circle in self.circles:
            s = s + circle.to_file() + "\n"

        for polyline in self.polylines:
            s = s + polyline.to_file() + "\n"

        for rect in self.rectangles:
            s = s + rect.to_file() + "\n"

        for text in self.texts:
            s = s + text.to_file() + "\n"

        for pin in self.pins:
            s = s + pin.to_file() + "\n"

        return s