class Date:
    # MONTS_LENGTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def add_year(self, year):
        self.year += year

    def add_month(self, month):
        self.add_year((self.month + month) // 12)
        self.month = (self.month + month) % 12

    def add_day(self, day):
        self.add_month((self.day + day) // 30)
        self.day = (self.day + day) % 30

    def __str__(self):
        return f"{self.day:0>2}/{self.month:0>2}/{self.year:0>4}"


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_hours(self, hours):
        days = (self.hours + hours) // 24
        self.hours = (self.hours + hours) % 24
        return days

    def add_minutes(self, minutes):
        self.add_hours((self.minutes + minutes) // 60)
        self.minutes = (self.minutes + minutes) % 60

    def add_seconds(self, seconds):
        self.add_minutes((self.seconds + seconds) // 60)
        self.seconds = (self.seconds + seconds) % 60

    def __str__(self):
        return f"{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}"


class Date_time(Date, Time):
    def __init__(self, years, months, days, hours, minutes, seconds):
        Date.__init__(self, years, months, days)
        Time.__init__(self, hours, minutes, seconds)

    def add_hours(self, hours):
        self.add_day(super().add_hours(hours))

    def __str__(self):
        return f"{self.day:0>2}/{self.month:0>2}/{self.year:0>4}\t{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}"


some_date = Date_time(2023, 10, 23, 10, 25, 30)
some_date.add_seconds(0)

print(some_date)

