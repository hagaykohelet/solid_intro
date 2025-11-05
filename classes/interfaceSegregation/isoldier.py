class IShoot:
    def shoot(self):
        print("shoot")

class INavigate:
    def navigate(self):
        print("nevigate")

class IAirSupportCaller:
    def callairsupport(self):
        print("call air support")


class Infantry(IShoot):
    pass

class ForwardObserver(INavigate):
    pass

class Pilot(IAirSupportCaller):
    pass