class Time:
    def __init__(self, hour, minute, second) -> None:
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def format(self, x):
        return x if x >= 10 else '0' + str(x)

    def print_out(self):

        print(f"{self.__hour:02d}: {self.__minute:02d}: {self.__second:02d} Hrs.")

def main():
    time1 = Time(12, 8, 6)

    time1.print_out()

main()
