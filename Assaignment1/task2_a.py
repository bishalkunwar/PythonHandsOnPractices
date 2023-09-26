# Author :- Bishal Kunwar 290, Date: 26th sept 2023

'''# Question: In this task, you need to write two Python scripts and run them from the system command line. Each script is worth 1.5 marks.
a) Creating a new output file and writing to it:
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" into it. Note that file write methods do not add newline characters to your strings. If you want to fully terminate the line in the file, add an explicit \n at the end of the string.'''

# Open a file in write mode ('w')
with open("newfile.txt", "w") as file:
    # Write the string to the file
    file.write("Hello file world!\n")  # Add '\n' to terminate the line

print("File 'newfile.txt' successfully created and wrote over")
