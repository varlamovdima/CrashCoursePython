from sys import argv

program_name , file_name = argv

# Opens with intent to read only
text = open(file_name)
# Read file as one string
total_file = text.read()
# Print contents of the file (total)
print(total_file)
# Close the file object
text.close()
# Re-open the file
text = open(file_name)
# Read the file as a collection of independent lines
lines = text.readlines()
# Print contents of the file (lines)
print(lines)
# Close the file object
text.close()

# Open file with intent to write
text = open(file_name,'w')
# Clear the file
text.truncate()

line1="1,2,3\n"
line2='4,5,6\n'
line3='7,8,9\n'

text.write(line1)
text.write(line2)
text.write(line3)
# Close the file object
text.close()

