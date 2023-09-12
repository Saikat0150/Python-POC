"""
Adapter Design Pattern -- is a structural design pattern
"""


class ConsoleWriter:
    def pprint(self, text):
        print(text)


class FileWriter:
    def write(self, text, file_name = 'output.txt'):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)


class WriterAdapter(object):
    def __init__(self, writer):
        self.writer = writer

    def write(self, *args):
        if isinstance(self.writer, ConsoleWriter):
            self.writer.pprint(*args)
        elif isinstance(self.writer, FileWriter):
            self.writer.write(*args)


if __name__ == "__main__":
    console_writer = ConsoleWriter()
    file_writer = FileWriter()

    writer1 = WriterAdapter(console_writer)
    writer2 = WriterAdapter(file_writer)

    writer1.write("output to the console.")
    writer2.write('output to the Output file')