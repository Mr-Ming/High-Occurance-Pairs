#!/usr/bin/python
# -*- coding: utf-8 -*-

from classes.permutation import Permutation

INPUT_FILE_PATH = 'Artist_lists_small.txt';
OUTPUT_FILE_PATH = 'outputFile.csv';
MINIMUM_OCCURANCE = 50;

def main():
  # Initialize the data_set which will hold the record from INPUT_FILE_PATH
  santize_data_set = []

  # Open INPUT_FILE_PATH file 
  with open(INPUT_FILE_PATH) as file:
    for row in file:

      # For each row it read, remove new line
      row = row.strip('\n')

      # Additionally, lets store each word in the string as an array item
      # ex: "Underground,Sleigh Bells,Belle" => ["Underground", "Sleigh Bells", "Belle"]
      row = row.split(',')

      santize_data_set.append(row)
  file.close

  # Use our permutation class to get all the permutation as well as return it in the following format
  # We want it to be in a pair of 2, must be sorted by the number of occurance from highest to lowest
  permutation = Permutation(santize_data_set)
  permutation_result = permutation.get_permutation_by_pair_order_by_occurance_descending()
  
  # Create the output file
  file_pointer = open(OUTPUT_FILE_PATH, "w")

  # Write the header
  file_pointer.write("Pairs, Occurance" + "\n")

  for pair, occurance in permutation_result:
    if (occurance >= MINIMUM_OCCURANCE) :
      file_pointer.write('"(' + pair[0] + ', ' + pair[1] + ')", ' + str(occurance) + '\n')

  print ('Successfully Generated ' + OUTPUT_FILE_PATH)

if __name__== "__main__":
  main()