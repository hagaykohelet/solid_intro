class Idrive :
    def drive(self):
        print("drive\n")

class IFly:
    def fly(self):
        print("fly")

class ISail:
    def sail(self):
        print("sail")

class Tank(Idrive):
    pass

class FighterJet(IFly, Idrive):
    def drive(self):
        print("on runway")


class Submarine(ISail):
    pass






