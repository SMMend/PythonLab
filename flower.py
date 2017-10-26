flowers=["rose", "lily", "palm", "violet"]
print flowers

##print individual items
##for i in range(0,4):
#	print "item", i, "is", flowers[i]


##using len
#for i in range(0, len(flowers)):
#	print "using len", i , flowers[i]

#for i in range(len(flowers)):
#	print "using len without 0", i , flowers[i]


#for i in range(len(flowers)):
#	flowers[i] =flowers[i] + " is a flower"
	#print "iteration", i, flowers
#print "overall", flowers

#for i in range(len(flowers)):
#	flowers[i]=flowers[i].strip("flower")
#	print flowers

#a="This is a sentence"
#a=a.replace("sentence", "")
#print a

#for i in range(len(garden)):
#	garden[i]=garden[i].replace("flower", '')
#	print garden

newflowers=["petunia flower", "orchid flower"]
garden =flowers + newflowers
print garden

garden.insert(0, "sunflower")
print garden

del garden[4]
print garden

garden.remove("palm")
print garden

#garden.pop()
#print garden


print "The original garden list is", garden
garden[2:4] =['pine apple', 'strawberry']
print "the new list is ", garden
garden.sort( reverse =True)
print "Sorted garden", garden

##Dictionaries
garden2={"a" : "sunflower", "b" : "rose", "c" : "tulip", "d" : "daisy", 4:"lily"}
print garden2["a"]

capitals ={'CA':'Sacremento', "NV":"Carson City", "WA":"Olympia", "NM":"Santa Fe", "OH":"Columbus", "MO":"Jefferson City"}
print capitals["NV"]
capitals["TX"]="Austin"
results ="FL" in capitals
print results
print capitals
capitals_list =["Sacremento", "Carson City"]


#print keys
print (capitals.values())
	
	#print values