#python code for encryption

# take path of the file as an input
file_name=input("Enter the file name:")

path = file_name

# taking encryption key as input
key = 12
		
# open file for reading purpose
fin = open(path, 'rb')
	
# storing file's data in variable "file"
file = fin.read()
fin.close()
	
# converting file into byte array to perform encryption easily on numeric data
file = bytearray(file)

# performing XOR operation on each value of bytearray
for index, values in enumerate(file):
        file[index] = values ^ key

# opening file for writting purpose

fin = open('encrypted.tmp', 'wb')
	
# writing encrypted data in image
fin.write(file)
fin.close()
