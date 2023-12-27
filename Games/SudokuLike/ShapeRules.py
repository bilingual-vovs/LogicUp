from Shape import Shape


class ShapeRules:
    def __init__(self):
        raise NotImplementedError("Abstract class can't be initialized")

    def insert(self):
        raise NotImplementedError("Can't call abstract method")

    def remove(self):
        raise NotImplementedError("Can't call abstract method")

    def isValid(self, shape:Shape):
        raise NotImplementedError("Can't call abstract method")
