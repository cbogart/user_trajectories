import csv
from collections import defaultdict

#        author ->           year ->     (eco, commits)
fave = defaultdict(lambda: defaultdict(lambda: ("", 0)))

inf = csv.DictReader(open("career_sorted_fixed.csv","r"))
outf = csv.writer(open("career_sorted_best.csv","w"))

for i in inf:
    if int(i["commits"]) > fave[i["author"]][i["year"]][1]:
        fave[i["author"]][i["year"]] = (i["ecosystem"], int(i["commits"]))
    elif int(i["commits"]) == fave[i["author"]][i["year"]][1]:
        print "Arbitrarily assigned", fave[i["author"]][i["year"]][0], "over", i["ecosystem"], "at", i["commits"], "commits for both by", i["author"],"in",i["year"]

for a in fave.keys():
    for y in fave[a].keys():
        outf.writerow([a,y,fave[a][y][0], fave[a][y][1]])
