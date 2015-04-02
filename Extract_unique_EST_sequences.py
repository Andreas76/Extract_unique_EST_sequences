#!/usr/bin/python

# import modules
import fileinput
import sys
from Bio import SeqIO

# Open the source file to be read (one line at a time)
Source_file = fileinput.input([sys.argv[1]])
# Open the fasta formatted AT protein file
Search_name = sys.argv[2]
# Create and open the result file
Result_file = open(sys.argv[3], "a")

# Variables, lists and dictionaries
EST_list = []
Result_list = []

# Create dictionary containing all protein sequences in fasta format, protein AT number is the key
handle = open(Search_name, "rU")
AT_protein_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))

print "Finished making the EST dictionary"

# Iterate through each line in the source file
for line in Source_file:
    Source_Line = line.split()
    
# Clean up the protein identifier to make it searchable
    Entries = Source_Line[32].split(";")
    
    # Save all unique entries to a temporary list
    for item in Entries:
        if item not in EST_list:
            EST_list.append(item)
            
print "Finished making list of unique EST's"
    
# Search for protein identifier in AT protein dictionary
for item in AT_protein_dict:
        if item in EST_list:
        
	    # Append the item to a new list
            Result_list.append(AT_protein_dict[item])

print "Finished searching for hits in protein dictionary"

# Write the result to file            
SeqIO.write(Result_list, Result_file, "fasta")

# Close open files     
handle.close()
Source_file.close()

print "End of script"
