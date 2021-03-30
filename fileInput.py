import os
from Bio import Entrez, SeqIO
Entrez.email = "ecrum@luc.edu"

curr_path = os.getcwd()


def getFasta(accession):
    # Creates a fasta CDS file from a provided genbank accession

    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()

    inSeq = curr_path + '/' + accession + '.fasta'
    getSeq = open(inSeq, 'w')
    for rec in record.features:     # iterate through list of features
        if rec.type == "CDS":
            getSeq.write(">" + str(record.id) + "\n")               # gene IDs
            getSeq.write(str(rec.extract(record.seq)) + "\n")       # gene sequence
    getSeq.close()


def parseFasta(file_path):
    # Opens fasta CDS files, parses them and returns a dictionary containing the gene name and sequence

    f = open(file_path, 'r')
    fs = f.read().strip().split('>')
    final_genes = {}
    for i in fs[1:]:
        si = i.split(' ')
        for comp in si:
            if 'gbkey' in comp:
                final_genes[si[0][4:]] = comp[12:].replace('\n', '')
    return final_genes


#create a definition to get the Key value for the dictionary
def GetKey(val):
   for key, value in dictA.items():
      if val == value:
         return key
      return "key doesn't exist"

#create a definition to take the parsed file from the Phage,
#and pull the coding sequence from the gene before breaking it into a list
#of codons
def phageCDS(phageGeneList):
    for gene in phageGeneList:
        codingseq = GetKey(gene)
        #create a list of the codons present in this gene
        codonlist = [codingseq[i:i+3] for i in range(0, len(codingseq), 3)]
        #loop through the codon list 
        for j in codonlist:
