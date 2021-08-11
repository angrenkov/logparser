class DateTime:

    MONTH_LIST = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12,

    }

    year = 0
    month = 0
    day = 0
    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, dateStr):
        if dateStr == '':
            return
        self.Parse(dateStr)

    def Parse(self, dateStr):
        self.year = int(dateStr[7:11])
        self.month = self.MONTH_LIST[dateStr[3:6]]
        self.day = int(dateStr[:2])
        self.hours = int(dateStr[12:14])
        self.minutes = int(dateStr[15:17])
        self.seconds = int(dateStr[18:20])

    def ArgDateParse(self, ArgDateStr):
        self.day = int(ArgDateStr[:2])
        self.month = int(ArgDateStr[3:5])
        self.year = int(ArgDateStr[6:10])
        self.hours = int(ArgDateStr[11:13])
        self.minutes = int(ArgDateStr[14:16])
        self.seconds = int(ArgDateStr[17:19])

    def DateToInt(self):
        return self.seconds + 60 * self.minutes + 3600 * self.hours + (24 * 3600) \
               * self.day + (30 * 24 * 3600) * self.month + (12 * 30 * 24 * 3600) * self.year