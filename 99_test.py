#for i in range(5, 0, -1):
#	print """{0} bottles of beer on the wall, {0} bottles of beer ... 
#	 If one of those bottles should happen to fall, {1} bottles of beer on the wall""".format(i, i-1)



#Fibonnaci sequence
n=[]
n3=0
for i in range(0, 2):
	if i < 2:
		n.append(i)
		print n
	else:
		n1=int(n.pop(i-1))
		n2=int(n.pop(i-2))
		n3=n1 + n2
		print "n1=" , n1 , "\nn2=", n2, "\nn3=", n3
		n.insert(i-2, n2)
		n.insert(i-1, n1)
		n.insert(i, n3)
		print n
print n


#movies
# Jurassic Park, PG-13, 3, 8.0, Adventure / Sci-Fi
# Back to the Future, PG, 1, 8.5, Adventure / Comedy / Sci-Fi

movie_titles=["Jurassic Park", "Back to the future"]
parental_guidance=["PF-13", "PG"]
bech=[2, 1]
imdb=[8.0, 8.5]
genre =["Adventure / Sci-Fi", "Adventure / Comedy / Sci-Fi"]

p=zip(movie_titles, parental_guidance, bech, imdb, genre)
print p
for i in range (0, len(p)):
	print p[i]

for i, j, k, l, m in zip(movie_titles, parental_guidance, bech, imdb, genre):
	print "2nd try", i, j, k, l, m