import sys

for x in range(0,999):
	for y in range(0,999):
		strx = str(x).zfill(3)
		stry = str(y).zfill(3)

		set1 = set(list(strx))
		set2 = set(list(stry))

		if len(set1) == 3 and len(set2) == 3 and len(set1 | set2) == 6:
			newset = {int(x)*int(y) for x in set1 for y in set2}
			if len(newset) == 5:
				print set1
				print set2
				print newset
				sys.exit()

			
