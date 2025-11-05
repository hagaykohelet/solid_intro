from abc import ABC,abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self,message):
        pass

class EmailNotifier(Notifier):
    def send(self,message):
        print(f"this is email message {message}")


class SMSNotifier(Notifier):
    def send(self,message):
        print(f"this is sms message {message}")

class PushNotifier(Notifier):
    def send(self,message):
        print(f"this is a push notifier {message}")

