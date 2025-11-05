# class BirdUnit:# זה דורס את המתודה הקיימת
#     def fly(self):
#         print("flying")
#
# class Drone(BirdUnit):
#     def fly(self):
#         print("can fly")
#
# class Tank(BirdUnit):
#     def fly(self):
#         print("cant fly")


class FlyingUnit :
    def fly(self):
        print("flying")

class GroundUnit:
    def ability(self):
        print("cant flying")

class Drone(FlyingUnit):
    pass

class Tank(GroundUnit):
    pass


