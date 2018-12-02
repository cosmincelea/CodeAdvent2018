import itertools

fileName = input('What is the name of the file my Dude?\n')
data = [float(x) for x in open(fileName).readlines()]
print("The Total freq is: " + str(sum(data)))

freq = 0
allFreqValues = set()
for val in itertools.cycle(data):
    freq = freq + val
    if freq in allFreqValues:
        print("The Repeatable freq is: " + str(freq)) 
        break
    allFreqValues.add(freq)