class Line:
    def __init__(self, c) -> None:
        self.c = c

    def print(self):
        print(self.c * 10)


line1 = Line("3")
line1.print()
