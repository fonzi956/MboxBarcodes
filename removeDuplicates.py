file = open("db.csv", "r")
newtexts = ""
ToF = False
pr = ""
barcode = []
duplicate = []
for line in file:
    for bc in line:
        if bc == ',':
            break
        pr += bc
    if pr not in barcode:
        barcode.append(pr)
        newtexts += line
        pr = ""
    else:
        duplicate.append(pr)
        pr = ""
        continue
newtexts += "\n\n duplicate: \n"
for i in duplicate:
    newtexts += i + "\n"
file.close()
newfile = open("newdb.csv", "w")
newfile.write(newtexts)
newfile.close 



