class Employee:

    def __init__(self, name, worked_times):
        """
        Parameters
        ----------
        name : str
        worked_times : list of DayWorkedTime
        """
        self.__name = name
        self.__worked_times = worked_times

    @classmethod
    def create_from_string(cls, input_string):
        name, worked_time_string = input_string.split("=")
        worked_time = [DayWorkedTime.create_from_string(worked_day) for worked_day in worked_time_string.split(",")]
        return cls(name, worked_time)

    @property
    def name(self):
        return self.__name

    @property
    def worked_time(self):
        return self.__worked_times

    def __str__(self):
        return f'Employee {self.name}'


class DayWorkedTime:
    __weekday = ""
    __start = None
    __end = None

    def __init__(self, weekday, start, end):
        self.__weekday = weekday
        self.__start = start
        self.__end = end

    @classmethod
    def create_from_string(cls, input_string):
        """
        Create DayWorkedTime object from a string with the format MO10:00-12:00
        """
        weekday = input_string[:2]
        start, end = input_string[2:].split("-")

        return cls(weekday, cls.str_time_to_int(start), cls.str_time_to_int(end))

    @classmethod
    def str_time_to_int(cls, value):
        """Convert str time in the format HH:MM to int

        Parameters
        ----------
        value : str

        Returns
        -------
        int
        """
        return int(value[:2])

    @property
    def weekday(self):
        return self.__weekday

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __str__(self):
        return f'DayWorkedTime {self.__weekday} from {self.start} to {self.end}'
