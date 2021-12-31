capacity = 5
pages =[1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 4, 3, 7, 6, 6, 5, 3, 2, 1, 2, 3, 6]
s = []

pageFaults = 0

for i in pages:
	if i not in s:

		# Check if the list can hold equal pages
		if(len(s) == capacity):
			s.remove(s[0])
			s.append(i)

		else:
			s.append(i)
		pageFaults +=1
	else:
		s.remove(i)
		s.append(i)
	
print("{}".format(pageFaults))
