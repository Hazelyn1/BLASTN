#Started 4/19/22
#!usr/bin/python3
#Hazelyn Cates
#This program parses through a BLASTN output file and prints the alignment number, accession number, length, and score
#of each alignment


import re
i = 1 #counter to only print first 10 alignment results

print("Enter full name of text file:")
file_name = input()
open_file = open(file_name, "r")

#open_file = open("example_blast.txt", "r")

for line in open_file:
    new_line = line.strip()

    #make the patterns their own variables to increase readability
    #Start with finding the Query ID:
    ID_pattern = r"y=\s(.+)"
    ID = re.search(ID_pattern, new_line)

    if ID:
        query_id = ID.group(1)
        print("Query ID: %s" % query_id)


    #next is query length:
    Qlength_pattern = r"Length=(\d+)"
    length = re.findall(Qlength_pattern, new_line)

    if length:
        print("Query length: %s\n" % length[0])
        break


for line in open_file:
    new_line = line.strip()

    #want to parse through file to find accession number:
    acc_pattern = r"\>(.+)\|\s"
    accession = re.search(acc_pattern, new_line)

    if accession:
        acc_num = accession.group(1)
        #print("Accession = %s|" % acc_num)

    #Next is alignment length, which is DIFFERENT from query length (see above)
    align_len_pat = r"Length=(\d+)"
    align_len = re.search(align_len_pat, new_line)

    if align_len:
        A_length = align_len.group(1)
        #print("Length = %s" % A_length)

    #last is score of each alignment
    score_pattern = r" \=\s{2,}(\d)+"
    score = re.search(score_pattern, new_line)

    if score:
        blast_score = score.group()
        #print("Score %s\n" % blast_score)

        print("Alignment #%d: Accession = %s| (Length = %s, Score%s)" % (i, acc_num, A_length, blast_score))

        i+=1 #once all if statements are completed, increment the counter by one
        if i == 11: #once the counter hits 11 meaning the first 10 results have been outputted,
            break #break out of the loop and end the program