first_name='abdullah'
last_name='khan'
#joining above string togather
full_name =first_name+" "+last_name
print(full_name)
#an other method to joing string 
print(first_name,last_name)
#repeat string
print(first_name * 3)
lough='ha'
print(lough * 3)
# finding lenghth of string means how many letter or charactor in it
print(len(first_name)) # count space ,letters, symbols
#indexing means get a latter by its number in the word (start at 0 from left, start at-1 from right) 
print(first_name[0]) # 1st letter
print(first_name[-1]) # last letter 
# slicing means cutt out a piece of strig 
print(first_name[0:3]) # 0 included and 3 not include [0 to 2 ]
print(first_name[3:]) # 3 to end 
print(last_name[-1:-2]) # does not giving any result(out put) it mean we will slicing by positive number only 
# change letters case 
print(first_name.upper()) #all capital letters 
print(first_name.capitalize())# 1st letter will be capital
print(first_name.lower())#all small letters
# memebership means check if something inside ( is a letter or word in the string?)
print('a'in first_name)
print( 'x'in first_name)
# replace letters or words 
print(first_name.replace('a','A')) # replacing 0ne letter 
print(first_name.replace('lah','khan')) # replacing multiple letters


# we can store replaced word into an other variable 
# for a sentence 
senetece='i love c++'
new_sentece= senetece.replace('c++','python')
print(new_sentece)
# split means break a sentece into words ( coverting a sentece into a list of words ) 
print(senetece.split())
# we can also store split into an other variable then print new variable 
list= senetece.split()
print(list)
print(first_name.split()) #(does not convert a word into list of letters included in word) only covert a sentece (multiple words ) into a list of word included in senetence
# join means join a lsit of words to  make a sentence (coverting a list of word into a sentence )
list1= ['i','love','python']
sentence1=" ".join(list1)
print(sentence1)
print(" ".join(list1))