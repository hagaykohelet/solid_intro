# class ICommSystem :
#     def sendRadio(self):
#         print("radio")
#
#     def sendSatellite(self):
#         print("send satellite")
#
#     def sendMorseCode(self):
#         print("send morse code")
#
# class FieldRadio(ICommSystem):
#     def sendSatellite(self):
#         pass
#     def sendMorseCode(self):
#         pass
#
#
# class SatelliteComm(ICommSystem):
#     def sendMorseCode(self):
#         pass
#     def sendRadio(self):
#         pass
#
# class LegacyMorseUnit(ICommSystem):
#     def sendSatellite(self):
#         pass
#     def sendRadio(self):
#         pass


class IRadioComm:
    def sendRadio(self):
        print("radio")

class ISatelliteComm:
    def sendSatellite(self):
        print("send satellite")

class IMorseComm:
    def sendMorseCode(self):
        print("send morse code")


class FieldRadio(IRadioComm):
    pass

class SatelliteComm(ISatelliteComm):
    pass

class LegacyMorseUnit(IMorseComm):
    pass


