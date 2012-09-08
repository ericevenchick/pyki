from pyki.component import Component

class SchematicLibrary:
    def __init__(self):
        self.version = None
        self.encoding = None
        self.components = []

    def open(self, filename):
        f= open(filename, 'r')
        self.from_file(f.readlines())
        f.close()

    def write(self, filename):
        f= open(filename, 'w')
        for line in self.to_file():
            f.write(line + "\n")
        f.close()

    def from_file(self, file_data):
        lib_params = file_data[0].strip().split(" ")
        self.version = lib_params[2]
        try:
            self.encoding = file_data[1].strip().split(" ")[1]
        except IndexError:
            # could not get version
            self.encoding = None

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

    def to_file(self):
        file_data = []

        file_data.append(("EESchema-LIBRARY Version "
                          "{version}").format(version = self.version))
        file_data.append("#encoding {enc}".format(enc = self.encoding))

        for component in self.components:
            file_data.append("#")
            file_data.append("# %s" % component.name)
            file_data.append("#")
            file_data.extend(component.to_file())
        
        file_data.append("#")
        file_data.append("#End Library")
        return file_data



