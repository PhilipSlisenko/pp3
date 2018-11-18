import math


def drawAChart(legend, values, maxLengthOfChart):
    legendLength = len(max(legend, key=len))
    maxValue = max(values)
    for l, v in zip(legend, values):
        print(l.rjust(legendLength) + ": " +
              "".join("#" for i in range(math.ceil(v / maxValue * maxLengthOfChart))))


languages = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
popularity = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
maxLengthOfChart = 40

drawAChart(languages, popularity, maxLengthOfChart)
