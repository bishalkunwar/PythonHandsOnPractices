# Author :- Bishal Kunwar 290, Date: 26th sept 2023

# b) Reading and printing the contents of the file:
# Write another script that opens myfile.txt, reads its contents, and prints them. Check whether the new file shows up in the directory where you ran your scripts. Also, test what happens when you add a different directory path to the filename passed to open. 


# Open the file in read mode ('r')
with open("newfile.txt", "r") as file:
    # Read and print the contents of the file
    file_contents = file.read()
    print("Contents of the file readed is: \n")
    print(file_contents)

# Testing with a different directory path
file_path = "a/b/c/newfile.txt"
try:
    with open(file_path, "r") as file:
        file_contents = file.read()
        print("\nContents of", file_path + ":")
        print(file_contents)
except FileNotFoundError:
    print("\nThe file", file_path, "does not exist or not found.")



# # Expected Result: Hello file world!
# Hello file world!
# && 
# The file a/b/c/newfile.txt does not exist or not found.