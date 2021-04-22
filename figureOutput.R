# read in the file (phage host codon correlation) to a data table (and remove the first four lines)
datatable <- read.table(file = 'phage_host_codon_correlation.txt', header = FALSE, sep = '\t', skip = 4)

#rename the columns in the data table
colnames(datatable) <- c("Gene", "Corr")

#download the ('ggplot2') package
library(ggplot2)

#use ggplot to create the box plot
dev <- ggplot(datatable, aes(y = Corr, x = "")) + geom_boxplot() + coord_flip() + ylab("Codon Correlation") + xlab('')

#save the file as a PNG
dev.print(file="corrPlot.png", device=png, width=800)