test = "This is a sample text"

#WRITING A FILE

#Context manager:
with open("test.txt", "w") as f: #Creates a file named as test.txt and includes contents from test
    f.write(test)

#Another method:
fp = open("test2.txt", "w")
fp.write(test)
fp.close()

#READING A FILE

#Context manager:
with open("test.txt", "r") as f: #reads a file named as test.txt and displays contents from it
    f.read(test)

#Another method:
fp = open("test2.txt", "r")
fp.read(test)
fp.close()

#APPENDING A FILE

#Context manager:
with open("test.txt", "a") as f: #appends more contents to file named as test.txt and displays contents from it
    f.write("sample text2")

#Another method:
fp = open("test2.txt", "a")
fp.write("Sample text3")
fp.close()