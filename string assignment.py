chrt1="v"
chrt2='0'
chrt3='5'  
chrt4=':'
# explaination  chrt1,chrt2,chrt3,chrt4 are variable , '=' is assignment operator "v","0", "5", ":" are values
print(chrt1,chrt2,chrt3,chrt4) # out put will be v 0 5 : 
# critical thinking
#  space is a character or not? 
# let check 
space=" "
print(len(space)) # out put= 1 answer is yes space is a charcter 
# every thing inside the qoutation are count character
# task 2 
fav_animal= 'cat' 
santance='cats are cute'
# "cat" and " cats are cute" are two strings 
print(fav_animal,santance) # out put = cat  cats are cute
#task3
firt_name="muhammad"
last_name="abdullah"
# joining first and last name with space 
full_name=firt_name+" "+ last_name # + use to join  string values of  variables " " use for space 
print(full_name) # out put= muhammad abdullah 
# let try without using " "
full_name=firt_name+last_name
print(full_name) # out put= muhammadabdullah (without space )
# task 4
laugh="ha"
# printing 5 time above value of  variable using *
print(laugh*5) # out put= hahahahaha
# task 5 indexing
python='PythonRocks'
# print 1st  character
print(python[0]) # out put=P (in python counting start from 0) 
# 4th character 
print(python[3]) # out put=h 
# last character 
print(python[-1]) # out put=s
# task 5 
coding="I love coding in python"
print(coding[2:6]) # out put = love (charcter 2 to 5) 6th character not inclueded 
print(coding[17:]) # out put=python (character 17 to last )
#  try another method
print(coding[-1:-6]) # this method does not work 
# opetional task
name='abdullah'
print('welcome'" " +name+ "!" *3)