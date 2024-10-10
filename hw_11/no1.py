class Clock:
    def __init__(self, h, m, s) -> None:
        self.setTime(h, m, s)

    def run(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
                if self.hh == 24:
                    self.hh = 0
        am_or_pm = "a.m" if self.hh < 12 else "p.m"
        print(f"Current Time => {self.hh:02d}:{self.mm:02d}:{self.ss:02d} {am_or_pm}")

    def setTime(self, h, m, s):
        if h >= 24 or m >=60 or s >= 60:
            raise ValueError("Invalid Time Values!")
        self.hh, self.mm, self.ss = h, m , s

class AlarmClock(Clock):
    def __init__(self, h, m, s, alarm_hh, alarm_mm, alarm_ss) -> None:
        super().__init__(h, m, s)
        self.setAlarmTime(alarm_hh, alarm_mm, alarm_ss)

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
        self.alarm_on_off = True

    def alarm_on(self):
        self.alarm_on_off = True

    def alarm_off(self):
        self.alarm_on_off = False

    def run(self):
        super().run()
        am_or_pm = "a.m" if self.alarm_hh < 12 else "p.m"
        print(f"Alarm Time => {self.alarm_hh:02d}:{self.alarm_mm:02d}:{self.alarm_ss:02d} {am_or_pm}")
        if self.check_alarm_time():
            print("Alarm is ringing.")
            self.alarm_on_off = False

    def check_alarm_time(self):
        return self.alarm_on_off and self.alarm_hh == self.hh and self.alarm_mm == self.mm and self.alarm_ss == self.ss



def main():
    clock = Clock(0, 0, 0)
    clock.setTime(9, 8, 7)
    clock.run()

    alarm_clock = AlarmClock(0, 0, 0, 0, 0, 0)
    alarm_clock.setTime(3, 5, 59)
    alarm_clock.setAlarmTime(3, 6, 0)
    # alarm_clock.alarm_off()
    alarm_clock.run()

main()
