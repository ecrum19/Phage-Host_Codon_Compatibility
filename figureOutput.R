packages <- c("ggplot2", "optparse")
install.packages(setdiff(packages, rownames(installed.packages())), repos = "http://cran.us.r-project.org")  
library("optparse")
library("ggplot2")

option_list = list(
  make_option(c("-p", "--phageacc"), type="character", default=NULL, help="phage query accession", metavar="character")
);

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

cwd <- getwd()

figure<-function(phageacc)
{
  file <- paste(cwd, '/phage_host_codon_correlation.txt', sep='')
  data <- read.table(file = file, header = FALSE, sep = '\t', skip = 4)
  colnames(data) <- c("Gene", "Corr")
  data
  ggplot(data, aes(y = Corr, x = '')) + geom_violin(trim=FALSE, fill="gray") + ylab("Codon Correlation") + 
    xlab(phageacc) + geom_boxplot(width=0.1) + theme_classic()
  ggsave(paste(cwd, "/phage_gene_cc.png", sep=''))
}

figure(opt$phageacc)
