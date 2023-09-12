"""
Command Design Pattern - This is behavioural design pattern.
"""
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")


class EMAILCommand(BaseCommand):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_email(self.data)


class SMSCommand(BaseCommand):
    def __init__(self, receiver, data):
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_sms(self.data)


class NotificationService(object):
    """
    Receiver class
    """
    def send_email(self, data):
        print("Sending email", data)

    def send_sms(self, data):
        print("Sending short message", data)


class NotifivationInvoker(object):
    """
    Invoker Class
    """
    def __init__(self):
        self.notification_history = []

    def invoke(self, command):
        self.notification_history.append(command)
        command.execute()


if __name__ == "__main__":
    invoker = NotifivationInvoker()
    receiver = NotificationService()
    invoker.invoke(EMAILCommand(receiver, {"subject": "Test Email"}))
    invoker.invoke(SMSCommand(receiver, {"subject": "Test SMS"}))
    print(invoker.notification_history)
