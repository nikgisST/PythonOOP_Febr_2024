from abc import abstractmethod, ABC


class IContent(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        ...


class IProtocol(ABC):

    def __init__(self, sender: str, receiver: str):
        self.sender = sender
        self.receiver = receiver

    @abstractmethod
    def format_sender(self):
        ...

    @abstractmethod
    def format_receiver(self):
        ...


class IM(IProtocol):

    def format_sender(self):
        return ''.join(["I'm ", self.sender])

    def format_receiver(self):
        return ''.join(["I'm ", self.receiver])


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol: IProtocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IProtocol):
        self.__sender = sender.format_sender()

    def set_receiver(self, receiver: IProtocol):
        self.__receiver = receiver.format_receiver()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


protocol = IM("qmal", "james")
email = Email(protocol)

email.set_sender(protocol)
email.set_receiver(protocol)

content = HTML('Hello, there!')

email.set_content(content)
print(email)


