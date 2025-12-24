#open() - open the file 
# write() - write text (delete the existing text and insert current text)
file = open("demo.txt","w") 
file.write("This is Demo file")
file.close

#read() - read all content 
file = open("demo.txt" , "r")
print(file.read())
file.close

# append (a) mode - insert the text at the end 
file = open("demo.txt" , "a")
file.write("\nwelcome to demo file")
file.close

#readline() - read each line or single line at a time 
file = open("demo.txt" , "r+")
print(file.readline())
file.close

#readlines() - reeturns list of lines existed in the file 
file = open("demo.txt" , "r+")
print(file.readlines())
file.close

# reading lines in the file using for loop
file = open("demo.txt" , "r+")
for lines in file:
    print(lines)
file.close

#using with keyword 
with open("demo.txt" , "r") as f:
    print(f.read())

