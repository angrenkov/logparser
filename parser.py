from LogAnalyzer import LogAnalyzer
import sys

logs = LogAnalyzer(sys.argv)
logs.OpenFile()
logs.Parse()
logs.FilterByDate()

print(f'Requests: {logs.GetRequestCount()}')
print(f'Average requests count per second: {logs.GetAverageRequestsPerSecond()}')
print(f'Count of individual response codes: {logs.GetUniqueResponseCodeCount()}')
print(f'Average responses size: {logs.GetAverageResponsesSize()}')