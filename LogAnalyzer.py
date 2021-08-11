from DateTime import DateTime
from LogFilter import LogFilter


class Log:
    code = ''
    date = DateTime
    response_size = 0

    def __init__(self, log):
        self.Parse(log)

    def Parse(self, log):
        self.code = ''.join(log.split()[13:14])
        self.date = DateTime(''.join(log.split()[8:9])[1:])
        self.response_size = int(''.join(log.split()[-1:]))



class LogAnalyzer:

    log_list = []
    path_to_log_file = ''
    filter = LogFilter()
    filtered_logs = []
    logs = []

    def __init__(self, args):
        self.ParseArgs(args)

    def OpenFile(self):
        with open(self.path_to_log_file, 'r') as data_file:
            self.logs = data_file.readlines()

    def ParseArgs(self, args):
        iterator = 0

        for arg in args:
            if arg == '--from':
                parsed_date = DateTime('')
                parsed_date.ArgDateParse(args[iterator + 1])
                self.filter.date_from = parsed_date
            elif arg == '--to':
                parsed_date = DateTime('')
                parsed_date.ArgDateParse(args[iterator + 1])
                self.filter.date_to = parsed_date
                self.path_to_log_file = args[iterator + 2]
            iterator += 1

    def Parse(self):
        for line in self.logs[1:]:
            log_line = Log(line)
            self.log_list.append(log_line)

    def FilterByDate(self):
        for log in self.log_list:
            int_date = log.date.DateToInt()
            if self.filter.date_from.DateToInt() <= int_date <= self.filter.date_to.DateToInt():
                self.filtered_logs.append(log)

    def GetRequestCount(self):
        if len(self.filtered_logs) == 0:
            return 'No info'
        return len(self.filtered_logs)

    def GetAverageRequestsPerSecond(self):
        seconds_count = 1
        if len(self.filtered_logs) == 0:
            return 'No info'
        buf_seconds = self.filtered_logs[0].date.DateToInt()

        for log in self.filtered_logs:
            if log.date.DateToInt() != buf_seconds:
                seconds_count += 1
                buf_seconds = log.date.DateToInt()
        return self.GetRequestCount() / seconds_count

    def GetUniqueResponseCodeCount(self):
        if len(self.filtered_logs) == 0:
            return 'No info'

        codes = {

        }

        for log in self.filtered_logs:
            if codes.get(log.code) is None:
                codes[log.code] = 1
            else:
                codes[log.code] += 1
        return codes

    def GetAverageResponsesSize(self):
        if len(self.filtered_logs) == 0:
            return 'No info'
        response_count = 0
        for responses in self.filtered_logs:
            response_count += responses.response_size
        return response_count / self.GetRequestCount()