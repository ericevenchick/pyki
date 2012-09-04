from pyki.component import Component

class SchematicLibrary:
    def __init__(self, filename):
        self.filename = filename
        self.version = None
        self.date_str = ""
        self.encoding = None
        self.components = []

    def open(self):
        self.file = open(self.filename, 'r')
        self.from_file(self.file.readlines())
        self.file.close()

    def from_file(self, file_data):
        in_component = False
        component_data = []

        for line in file_data:
            params = line.strip().split(" ")
            # check for the start of a component definition
            if params[0] == "DEF":
                in_component = True

            if in_component:
                component_data.append(line)

            # check for the end of a component definition
            if params[0] == "ENDDEF":
                in_component = False
                c = Component()
                c.from_file(component_data)
                self.components.append(c)
                component_data = []




