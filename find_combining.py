import unicodedata
import codecs
import pdb
import csv

ZALGO_CHAR_CATEGORIES = ['Mn', 'Me']

csvf = csv.writer(open("career_sorted_fixed.csv","w"))
with codecs.open("career_sorted.csv", 'r', 'utf-8', 'replace') as infile:
    for line in infile:
        fixed = ""
        for c in unicodedata.normalize('NFD', line):
            if unicodedata.category(c) not in ZALGO_CHAR_CATEGORIES:
                fixed += c
            else:
                fixed += "#"
        
        #fixed = ''.join([c for c in unicodedata.normalize('NFD', line) if unicodedata.category(c) not in ZALGO_CHAR_CATEGORIES])
        fixed = fixed.replace("\\","\\\\").encode("utf-8").strip()
        parts = fixed.split(",")
        splitty = [ ','.join(parts[:-3])] + parts[-3:]
        if len(splitty) != 4: 
            print "skipping", line
        else:
            csvf.writerow(splitty)
