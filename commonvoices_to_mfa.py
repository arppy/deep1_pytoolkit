import re

description_file_name = "/home/berta/data/cv-corpus-17.0-2024-03-15/hu/validated.tsv"

with open(description_file_name) as description_file:
   next(description_file)
   for line in description_file:
      split_line = re.split(r'\t+', line)
      print(split_line[0], split_line[1], split_line[3])
      break
