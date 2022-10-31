import os
import shutil


#Prompt user to input the directory where there images are at
print("Enter file location:")
file_location = input()



#Collect a list of files in that directory and return a list for the user to see.
files_collected = []
for path in os.listdir(file_location):
    if os.path.isfile(os.path.join(file_location, path)):
        files_collected.append(path)

print("Renaming the following files:", files_collected)



#Prompt the user to chose a name for their new folder 
print("Enter new name for your new folder: ")
new_folder = input()

#Prompt the user to chose a new name for their files
print("Enter a new name for your files: ")
new_prefix = input()

#Prompt the user to chose what file extension they want their new files in
print("Enter file extension (jpg, png, etc): ")
file_extension = input()



#Create a new folder based on previous inputs
new_destination = os.path.join(file_location, new_folder)
if not os.path.exists(new_destination):
    os.mkdir(new_destination)



#Make a new copy of the files, rename them, and place them in the new folder.
for count, file_name in enumerate(os.listdir(file_location)):
    dst = new_prefix + "_" + str(count) + "." + file_extension
    old_name = os.path.join(file_location, file_name) 
    new_name = os.path.join(new_destination, dst)
    shutil.copy(old_name, new_name)



#Zip the new folder up
shutil.make_archive(new_folder,"zip", file_location)
