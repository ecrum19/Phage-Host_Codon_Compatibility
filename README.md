# Phage-Host_Codon_Compatibility

## Dependenices:

**Software:**

Linux

R -- https://www.r-project.org/

Pyhton 3 -- https://www.python.org/downloads/



**Python Packages:**

BioPython -- https://biopython.org/wiki/Download

Pandas -- https://pandas.pydata.org/

SciPy -- https://scipy.org/install.html


## **Instructions:**

1. Download all files into a directory (Use command: git clone https://github.com/ecrum19/Phage-Host_Codon_Compatibility.git)

2. Navigate to the directory containing the the downloaded repo files

3. Execute the command: python3 phcc.py -s XXX -q XXX
        
        Arguments:
        
        -s AA012345.1    (RefSeq Accession of bacterial genome or file path to bacterial CDS fasta file)
        -q A01234.1      (RefSeq Accession of phage genome or file path to phage CDS fasta file)


**Files used for testing:**
    
    Bacteria 1 (Ecoli_bacteria.txt) -- E. coli K12 strain C3026; RefSeq Accession: CP014272.1
    Bacteria 2 (Strep_bacteria.txt) -- Streptococcus pneumoniae AP200; RefSeq Accession CP002121.1
    Phage 1 (Lambda_phage.txt) -- Escherichia phage lambda; RefSeq Accession: J02459.1
    Phage 2 (Lacto_phage.txt) -- Lactobacillus plantarum bacteriophage LP65; RefDeq Accession: AY682195.1

**For Test Runs:**

    Accession Based Tests:
    Positive Control: python3 phcc.py -s CP014272.1 -q J02459.1
    Negative Control (Bacteria): python3 phcc.py -s CP002121.1 -q J02459.1
    Negative Control (Phage): python3 phcc.py -s CP014272.1 -q AY682195.1
    
    File Based Tests:
    Positive Control: python3 phcc.py -s Ecoli_bacteria.txt -q Lambda_phage.txt
    Negative Control (Bacteria): python3 phcc.py -s Strep_bacteria.txt -q Lambda_phage.txt
    Negative Control (Phage): python3 phcc.py -s Ecoli_bacteria.txt -q Lacto_phage.txt
