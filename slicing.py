text = "My GitHub handle is @shannonturner and my Twitter handle is @svt827"

# Let's extract the GitHub handle using str.find() and slicing.

snail_index = text.find('@')

print text[snail_index:snail_index + 14] # So the first slicing index is given by the variable, but we're still relying on knowing the exact number of characters (14).  We can improve this.

space_after_first_snail_index = text[snail_index:].find(' ') # Note that we're using slicing here to say start the .find() after the first snail is found.

print text[snail_index:snail_index + space_after_first_snail_index] # Why do we need to add snail_index to the second slicing index? Take a look:

print "snail_index is: ", snail_index
print "space_after_first_snail_index is: ", space_after_first_snail_index

print "So this is essentially saying text[20:34], see? --> ", text[20:34]

# Instead of creating a separate variable, you can just add the str.find() that gives the number you want right into the slice, like this:

print text[text.find('@'):text.find('@')+text[text.find('@'):].find(' ')] # But as you can see, it's not the most readable, especially compared to above.
 
# Still, it's a fairly common syntax / notation, so it's worth being familiar with it and knowing what it looks like in case you run into it.

print "Can you use slicing and string methods like str.find() to extract the Twitter handle from text?"


