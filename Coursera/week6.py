#6.5 Write code using find() and string slicing (see section 6.10) to extract 
#the number at the end of the line below.  Convert the extracted value to a 
#floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";

posOfNum = text.find('0.8475')#finds the start position of the number
numAsFloat =  float(text[posOfNum:])#using the start postion extract everything to the end of the string and convert into a float

print numAsFloat
