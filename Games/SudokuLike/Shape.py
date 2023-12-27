from ShapeRules  import ShapeRules

class Shape:
    def __init__(self, cells:list, rules:ShapeRules):
        self.cells:list = cells
        self.rules:ShapeRules = rules
