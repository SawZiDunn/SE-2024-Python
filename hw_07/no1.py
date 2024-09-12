class Clock:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def set_time(self, hour, minute, second):
        if 0 <= hour < 24 and 0 <= minute < 60 and 0<= second < 60:
            self.__hour = hour
            self.__minute = minute
            self.__second = second
            return
        print("Invalid Time Format!")
        
    
    def get_time(self):
        return self.__hour, self.__minute, self.__second
    
    def tick(self):
        self.__second += 1
        
        if self.__second == 60:
            self.__minute += 1
            self.__second = 0
            if self.__minute == 60:
                self.__hour += 1
                self.__minute = 0
                if self.__hour == 24:
                    self.__hour = 0
        
        
    def display(self):
        am_pm = "a.m" if self.__hour < 12 else "p.m"
        if self.__hour > 12:
            hour = self.__hour - 12
        elif self.__hour == 0:
            hour = 12
        else:
            hour = self.__hour
        print(f"{hour:02d}: {self.__minute:02d}: {self.__second:02d} {am_pm}")
        
def main():
    clock = Clock(23, 8, 10)
    print(clock.get_time())
    
    '''
	If we use double underscore and try to access it using clock.__hour, we can also print clock.__hour later.
	But, if we don’t change the value using clock.__hour and try to print clock__hour directly, it will throw error.
    That's how private attribute works in python OOP.
    It works only for double underscore.
    '''
    # clock.__hour = 8
    # print(clock.__hour)
    
    clock.set_time(22, 59, 59)
    clock.tick()
    clock.display()
    
    clock.set_time(11, 59, 59)
    clock.tick()
    clock.display()
    
main()