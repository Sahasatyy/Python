#Strings are immutable i.e cannot change the original string through methods.
str1 = "SahasAmAtya"
print(str1.lower()) #converts to lower case
print(str1.upper())#converts to upper case
print(len(str1))# shows the length of the value in str1
print(str1.isalpha())#detects if the variable consist of A-Z, a-z elements only or not.

str2 = "SahasAmatya!!"
print(str2.rstrip("!")) #removes "!" from str2
print(str2.isalnum()) #detects if the variable consist of A-Z, a-z, 1-9 elements only or not.

str3 = "messi is the best playEr in the worLd"
print(str3)
print(str3.replace("messi","leo")) #replaces messi with leo
print(str3.split( )) #converts str3 into list and each word seperated via space is added as list elements.
print(str3.capitalize())#Capitalizes initial letter
print(str3.center(50))#prints st3 50pts to the center
print(len(str3.center(100)))#prints st3 100pts to the center
print(len(str3))# shows the length of the value in str1
print(str3.count("the")) #counts no of repetation of the word in str3
print(str3.endswith("worLd"))#Shows if the value given ends with worLd
print(str3.endswith("universe"))#Shows if the value given ends with universe
print(str3.find("best"))#locates 'best' word in str3 and gives its index num
print(str3.islower())#finds if given values are in lower case
print(str3.swapcase())#swaps lower case with upper case and viceversa.
