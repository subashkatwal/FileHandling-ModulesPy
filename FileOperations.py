#TO read a file in python 
# f=open('demo.txt',"r")
# print(f.read())

#Return the 5 first characters of the file
'''
f=open("demo.txt","r")
print(f.read(5))
print(f.readline())
f.close()
'''

#Loop through the file 
# for x in f:
#     print(x)


 
#Append the files
""" f=open("demo2.txt","a")
f.write("Now I've added this line too ")
f.close()

f=open("demo2.txt","r")
print(f.read())  """


#Write in the files

"""
    
    
f=open("demo3.txt","w")
f.write("Whoops! I've deleted the file ")
f.close()

f=open("demo3.txt","r")
print(f.read())
   
"""

#Create a file using 'x'
#f=open("myFile.txt","x")


#delete the file 
"""import os 
os.remove("myFile.txt")"""

#Check if file exists then deleting it 
import os 
if os.path.exists('demo3.txt'):
    os.remove("demo3.txt")
else:
    print("The file doesn't exists!")
    
    
#Creating a folder and deleting a folder 
""" 
import os 
#Create a folder using os 
os.makedirs("Subash")
#Removing the created folder 
os.rmdir("Subash")

"""


#Creating a multiple folders(directories) 

directories={
    'Folder1',
    'Folder2',
    'Folder3',
    'Folder4'
}


#Create a multiple folders
for directory in directories:
    os.makedirs(directory,exist_ok=True)
    print(f"The directories '{directory}'has been created")

#Deleted a multiple folders 
for directory in directories:
    os.removedirs(directory)
    print(f"The folder '{directory}' has been deleted ")





