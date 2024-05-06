#! /bin/bash
#basic tokenizer
awk -F"\t" '{split(tolower($2),a, /[ ,‚.?!;"“„”’‘:\x27…¬–-]/);for(i in a){suma[a[i]]++}}END{for(i in suma){print(i)}}' validated_sentences.tsv > validated_words.txt