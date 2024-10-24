# BLASTN
This script parses through a BLASTN output file and prints the query ID, query length, alignment number, accession number, length, and scores of the first 10 alignments.

The BLASTN output file to be parsed through must be in .txt format. An example file, "example_blast.txt", has been provided.

The program begins with reading in the user's input file, which must be in .txt format. A for loop starts by going through the file line by line, and starts by finding the query ID using regex. When found, the query ID is printing to the terminal. The program then searches for the query length, also using regex. When found, the query length is printed to the terminal. 
Once all the lines of the file have been parsed through, the program enters a second for loop which also goes through the file line by line. In this loop, the first task is to find the accession number of the BLASTN output result, which is accomplished using regex, then to find the alignment length and then to find the alignment score. Each is found using regex and stored in separate variables. 
Since BLASTN output automatically places the highest scores at the top of the alignment results, the top ten search results are printed to the terminal in descending order. Once the counter (i) hits 11, meaning the top 10 results have been printed out, the loop breaks and the program ends.  
