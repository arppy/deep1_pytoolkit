import re
import os

corpus_folder= "/home/berta/data/cv-corpus-17.0-2024-03-15/hu/"
original_clips_folder="clips/"
clips_folder="clips_by_user_with_text/"
try:
   os.makedirs(corpus_folder + clips_folder)
except FileExistsError:
   pass
description_file_name = "validated.tsv"

with open(corpus_folder + description_file_name) as description_file:
   next(description_file)
   for line in description_file:
      split_line = re.split(r'\t+', line)
      client_folder= split_line[0][:25] + "/"
      try:
         os.makedirs(corpus_folder + clips_folder + client_folder)
      except FileExistsError:
         pass
      clip_name = split_line[1]
      base_clip_name = clip_name.rsplit('.', 1)[0]
      os.system('cp '+corpus_folder+original_clips_folder+clip_name+' '+corpus_folder+clips_folder+client_folder+clip_name)
      lab_file_name = corpus_folder + clips_folder + client_folder + base_clip_name + ".lab"
      with open(lab_file_name, 'w') as lab_file:
         print(split_line[3], file=lab_file)
