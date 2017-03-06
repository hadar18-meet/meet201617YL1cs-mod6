#Module 6, Part 5: Practice with dictionaries here


my_phonebook={"Statue of Liberty":2125555555, "Ghostbusters":2125551234}

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
###

###
#Print the variable, num
###
my_phonebook["Statue of Liberty"]
###
#Change the value of the Ghostbusters' phone number to 2125559876
###
my_phonebook["Ghostbusters"] = 2125559876
#Here's an empty dictionary
your_phonebook={}

###
#Add 5 values to it like this
#your_phonebook['key']=value
###
your_phonebook[1]="1"
your_phonebook[2]="2"
your_phonebook[3]="3"
your_phonebook[4]="4"
your_phonebook[5]="5"

###
#Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys

#Loop over this sequence with a for loop
#using syntax like

#for key in sequence_of_keys :
#    #Do stuff
for key in your_phonebook:
    print( str(key) + ":" + your_phonebook[key])
#Use the loop to print to the shell the key and value
#of every element in the dictionary
###

