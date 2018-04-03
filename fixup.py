import csv

scanf = csv.reader(open("career_sorted.csv","r"))
outf = csv.writer(open("career_sorted_fixed.csv","w"))
for r in scanf:
    if len(r) > 4:
        names = ",".join(r[0:4])
        r = [names] + r[-3:]
    r[0] = r[0].replace("\\","\\\\")
    r[0] = repr(r[0].decode("utf-8","replace").encode("utf-8","replace"))
    if len(r[0]) > 250: r[0] = r[0][:250]
    outf.writerow(r)
    
