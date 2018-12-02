import string

arrayDict = []
with open('input.txt') as f:
	twoTimes = 0
	threeTimes = 0
	for line in f:
		cleanedLine = line.strip()
		d = dict.fromkeys(string.ascii_lowercase, 0)
		two = 0
		three = 0
		arrayDict.append(list(cleanedLine))
		for c in cleanedLine:
			d[c] += 1
		for v in d:
			if d[v] == 2:
				two = 1
			elif d[v] == 3:
				three = 1
		twoTimes += two
		threeTimes += three


	print ( threeTimes * twoTimes )


	for element in arrayDict:
		for element2 in arrayDict:
			if element2 != element:
				numberOfDiferences = 0
				differentLetter = False
				for index,ch in enumerate(element2):
					if element2[index] != element[index]:
						numberOfDiferences += 1
						differentLetter = element2[index]

				if numberOfDiferences == 1:
					print(''.join(element2) + '----' + ''.join(element) + '---' + differentLetter)
					

