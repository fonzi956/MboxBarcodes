file = open("Embc.txt", "r")
newtexts = ""
ToF = False
pr = ""
lis = []
for line in file:
    # if ("From " in line):
    #     # newtexts += line
    #     ToF = True
    # elif ("Content-Type: text/plain;" in line):
    #     ToF = False
    #     # continue
    # elif (line[0:2] == "--" in line):
    #     ToF = True
    # elif ("Content-Type: text/html;" in line):
    #     ToF = True
    # # for this part if statement with Content must be Content-Type: text/plain; continue
    # elif ("+---------- Forwarded message ----------+" in line):
    #     ToF = True
    # elif ("To: " in line):
    #     ToF = False
    # if (ToF == False):
    #     newtexts += line
    # # else:
    # #     newtexts += line

    
    # if (line[0:5].isnumeric()):
    #     line = line.replace(" ", "\", \"")
    #     newtexts += "\"" + line[:-1] + "\"\n"
    # else:
    #     newtexts += line

    # if ("all " in line):
    #     ToF = True
    #     pr = line[4:]
    #     newtexts += line
    #     continue
    # elif (ToF and line[0].isnumeric()):
    #     line = line.replace("\n", "")
    #     newtexts += line + " " + pr
    # else:
    #     ToF = False
    #     newtexts += line

    # if ("all " in line):
    #     continue
    # else:
    #     newtexts += line

    # if (not " " in line and line[0].isnumeric()):
    #     line = line.replace("\n", "")
    #     newtexts += line + " idk\n"
    # else:
    #     newtexts += line

    if (not line[0].isnumeric() and not line == "\n"):
        ToF = True
        pr = line.replace("\n", "")
        continue
    elif (ToF and line[0].isnumeric()):
        line = line.replace("\n", "")
        line = line.replace(" ", "\", \"")
        newtexts += "\"" + line + "\", \"" + pr + "\", \"\", \"\", \"\"\n"
    elif (line == "\n"):
        continue
    else:
        ToF = False
        newtexts += line

    # if (not line[0].isnumeric()):
    #     if (line == ""):
    #         continue
    #     else:
    #         if(not line in lis):
    #             lis.append(line)
    
for i in lis:
    newtexts += i
file.close()
newfile = open("NewEmBc.txt", "w")
newfile.write(newtexts)
newfile.close 



