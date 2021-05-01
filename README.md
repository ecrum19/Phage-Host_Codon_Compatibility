# Phage-Host_Codon_Compatibility

## Dependenices:

**Software:**

* Linux

* R -- https://www.r-project.org/

* Pyhton 3 -- https://www.python.org/downloads/



**Python Packages:**

* BioPython -- https://biopython.org/wiki/Download

* Pandas -- https://pandas.pydata.org/

* SciPy -- https://scipy.org/install.html


**R Packages:**

* Optparse -- https://cran.r-project.org/web/packages/optparse/index.html

* ggplot2 -- https://cran.r-project.org/web/packages/ggplot2/index.html


## **Instructions:**

1. Download all files into a directory (Use command: git clone https://github.com/ecrum19/Phage-Host_Codon_Compatibility.git)

2. Navigate to the directory containing the the downloaded repo files

3. Execute the command: python3 phcc.py -s XXX -q XXX (where Xs are replaced by accessions or local file paths)
        
        Arguments:
        
        -s AA012345.1    (RefSeq Accession of bacterial genome or file path to bacterial CDS fasta file)
        -q A01234.1      (RefSeq Accession of phage genome or file path to phage CDS fasta file)

**It is recommmended to run one of the test runs below before utilizing the pipeline for any non-test data.** 

### Test Runs:
**Included Test Input Files**
    
    Bacteria 1 (Ecoli_bacteria.txt) -- E. coli K12 strain C3026; RefSeq Accession: CP014272.1
    Bacteria 2 (Strep_bacteria.txt) -- Streptococcus pneumoniae AP200; RefSeq Accession CP002121.1
    Phage 1 (Lambda_phage.txt) -- Escherichia phage lambda; RefSeq Accession: J02459.1
    Phage 2 (Lacto_phage.txt) -- Lactobacillus plantarum bacteriophage LP65; RefDeq Accession: AY682195.1
    
**Copy and paste a command below for an example of a pipline run.**

    Accession Based Tests:
    Positive Control: python3 phcc.py -s CP014272.1 -q J02459.1
    Negative Control (Bacteria): python3 phcc.py -s CP002121.1 -q J02459.1
    Negative Control (Phage): python3 phcc.py -s CP014272.1 -q AY682195.1
    
    File Based Tests:
    Positive Control: python3 phcc.py -s Ecoli_bacteria.txt -q Lambda_phage.txt
    Negative Control (Bacteria): python3 phcc.py -s Strep_bacteria.txt -q Lambda_phage.txt
    Negative Control (Phage): python3 phcc.py -s Ecoli_bacteria.txt -q Lacto_phage.txt


## Output Files

Below are the output files (in order of production by the pipeline)

**Intermediate Files:**
* Input_Accession.fasta -- (Only produced if accession is used) CDS fasta file created from GenBank record
* phageGeneCodons.txt -- Codon frequencies for every phage gene from CDS fasta (either inputted or created from provided accession)
* matches -- BLASTx hits returned by DIAMOND (bacterial CDSs as query, provided db of known HEG proteins as subject)
    * Format of file: stitle bitscore qtitle
* HEGS.fasta -- List of highly expressed genes (HEGs) identified from the bacteria via the matches file
* bacteriaHEGCodons.txt -- Codon frequencies for every bacterial HEG from HEGS.fasta
* nohup.out -- Unwanted, verbose print statements from running wget and DIAMOND

**Informative Files:**
* AbnormalCodonReport.txt -- (Only produced if abnormal phage codons are found) Information about codons containing non-conclusive bases (anything not A,C,G,T)
* phage_gene_cc.png -- Visual violin/box plot representation of Phage gene codon correlations
* phage_host_codon_correlation.txt -- Summary of pipeline results
      
      Format: 
      Bacteria_record \t Phage_record
      
      Global codon correlation
      
      Phage gene (protein ID) \t Codon correlation
      ...



