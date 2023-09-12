"""
strategy Design Pattern - is a behavioural design pattern
"""
from abc import *


# Strategy Interface
class PasswordStrategy(ABC):
    @abstractmethod
    def generate(self):
        pass


class AlphaPasswordStrategy(PasswordStrategy):
    def generate(self):
        return "abcdefghijklmnopqrstuvwxyz"


class NumericPasswordStrategy(PasswordStrategy):
    def generate(self):
        return '1234567890'


class DefaultStrategy(PasswordStrategy):
    def generate(self):
        return "abcde12345"


# Main Class
class PasswordGenerator:
    def generate_password(self, password_gen: PasswordStrategy):
        return password_gen.generate()


if __name__ == "__main__":
    pg = PasswordGenerator()
    password = pg.generate_password(AlphaPasswordStrategy())
    print("Your generated password is - ", password)