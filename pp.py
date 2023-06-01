import re
path = "input.txt"
file = open(path,"r")

##remove date and time
#con = file.read()
#pattern = r"\d\d\/\d\d\/\d\d\d\d,"
#text = re.sub(pattern,"",con)
#pattern = r"\d\d?:\d\d?\s[ap]m\s-"
#text = re.sub(pattern,"",text)

con = file.read()
file.close()
pattern = r"^.+-"
text = re.sub(pattern,"",con,flags=re.MULTILINE)
##media ommited
pattern = r".*\<Media omitted\>.*"
text = re.sub(pattern,"",text)

file = open("input_training2.txt","w")
file.write(text)
file.close()


print(text)
