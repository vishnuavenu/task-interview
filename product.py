class Product:
    def __init__(self, name, specs ):
        self.name = name
        self.specs = specs

    def setName(self, name ):
        self.name = name
        return self

    def setSpecs(self, specs):
        self.specs = specs
        return self

    def getName(self):
        return self.name

    def getSpecs(self):
        return self.specs

    def __str__(self):
        c = '\n'
        desc = "Product Name: \n"+self.name+"\nSpecs:\n"+c.join([spec for spec in self.specs])
        return desc.decode('utf8')