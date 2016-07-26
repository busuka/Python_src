from paiza import ImportCase
from collections import OrderedDict

p = ImportCase.auto_input("PlanWeather.txt")


def arrange_line(line):
    return list(map(int, line.split(" ")))


input_lines = arrange_line(p.__next__())
numHoliday = input_lines[0]
numTrip = input_lines[1]
ProbDict = OrderedDict()
numloop = numHoliday - numTrip + 1

for i in range(numHoliday):
    input_lines = arrange_line(p.__next__())
    ProbDict[input_lines[0]] = input_lines[1]

Prob_i = min(ProbDict.keys())
ans = Prob_i
max_sum = numTrip * 100

for i in range(numloop):
    Prosum = 0
    for ii in range(Prob_i, Prob_i + numTrip):
        Prosum += ProbDict[ii]
    if max_sum > Prosum:
        max_sum = Prosum
        ans = Prob_i
    Prob_i += 1

print(ans, ans+numTrip-1)
