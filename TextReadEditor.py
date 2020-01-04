
with open("backend.txt", "r") as fi:
	data = fi.readlines()
	format1 = ' '
	format1 = format1.join(data)

f1 = 'James Smith'
f2 = 'Thanks for buying'
f3 = 'Lever 2000 with Color Safe Bleach'



finalString = (format1.format(f1,f2,f3))

#finalString.replace(" ", "")
print (finalString)

input()
