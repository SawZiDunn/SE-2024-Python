class Time:
    def __init__(self, hour, minute, second) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def format(self, x):
        return x if x > 10 else '0' + str(x)

    def print_out(self):

        print(f"{self.format(self.hour)}: {self.format(self.minute)}: {self.format(self.second)} Hrs.")

def main():
    time1 = Time(12, 8, 6)
    time1.print_out()

main()