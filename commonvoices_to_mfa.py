import re
import os

corpus_dir="/home/berta/data/cv-corpus-17.0-2024-03-15/hu/"
clips_folder="clips_by_user_with_text/"
try:
   os.makedirs(corpus_dir+clips_folder)
except FileExistsError:
   pass
description_file_name = "validated.tsv"

with open(corpus_dir+description_file_name) as description_file:
   next(description_file)
   for line in description_file:
      split_line = re.split(r'\t+', line)
      print(split_line[0], split_line[1], split_line[3])
      try:
         os.makedirs(corpus_dir+clips_folder+split_line[0])
      except FileExistsError:
         pass
      clip_name = split_line[1]
      base_clip_name = clip_name.rsplit('.', 1)[0]
      print(corpus_dir+clips_folder+split_line[0]+"/"+base_clip_name+".lab")
      #with open(corpus_dir+clips_folder+split_line[0]+"/"+, 'a') as f:
      #   print('hello world', file=f)
      break
