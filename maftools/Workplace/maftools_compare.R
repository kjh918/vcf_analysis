library('maftools')
library('ggplot2')
library('openxlsx')
arg = commandArgs(TRUE)

file_1 = paste0(getwd(),'/Sample_step/',arg[1])
file_2 = paste0(getwd(),'/Sample_step/',arg[2])

data_1 <- read.maf(maf=file_1)
print(data_1)
t_vaf <- as.numeric(data_1@data$t_alt_count)/as.numeric(data_1@data$t_depth)
data_1@data <- cbind(data_1@data, t_vaf)
t_vaf <- as.numeric(data_1@maf.silent$t_alt_count)/as.numeric(data_1@maf.silent$t_depth)
data_1@maf.silent <- cbind(data_1@maf.silent, t_vaf)
sub_1 = subsetMaf(maf=data_1, query='t_depth >= 500')
sub_1 = subsetMaf(maf=sub_1, query='t_vaf >= 0.01')

data_2 <- read.maf(maf=file_2)
t_vaf <- as.numeric(data_2@data$t_alt_count)/as.numeric(data_2@data$t_depth)
data_2@data <- cbind(data_2@data, t_vaf)
t_vaf <- as.numeric(data_2@maf.silent$t_alt_count)/as.numeric(data_2@maf.silent$t_depth)
data_2@maf.silent <- cbind(data_2@maf.silent, t_vaf)
sub_2 = subsetMaf(maf=data_2, query='t_depth >= 500')
sub_2 = subsetMaf(maf=sub_2, query='t_vaf >= 0.01')

compare = mafCompare(m1=sub_1,m2=sub_2,m1Name=arg[1],m2Name=arg[2],minMut=5)
print(compare)
gsub('.maf','',arg[1])
gsub('.maf','',arg[2])

gene <- subset(compare$results,pval<0.05)
gene <- gene$Hugo_Symbol

print(gene)
# write.xlsx(compare,file=paste0(getwd(),'/',arg[1],'-',arg[2],'compare_result.xlsx'))
# forestPlot
png(paste0('~/kjh/',arg[1],'-',arg[2],' forestPlot.png'),1300,1300,res=150)
forestPlot(mafCompareRes = compare,pVal = 0.05, color = c('royalblue','maroon'))
dev.off()

# coOncoplot
png(paste0('~/kjh/',arg[1],'-',arg[2],' coOncoplot.png'),1300,1300,res=150)
coOncoplot(m1=sub_1,m2=sub_2,m1Name=arg[1],m2Name=arg[2],removeNonMutated=TRUE,showSampleNames=TRUE)
dev.off()

# coBarplot
png(paste0('~/kjh/',arg[1],'-',arg[2],' coBarplot.png'),1300,1300,res=150)
coBarplot(m1=sub_1,m2=sub_2,m1Name=arg[1],m2Name=arg[2])
dev.off()
# lollipopplot2
png(paste0('~/kjh/',arg[1],'-',arg[2],' lollipopPlot.png'),1300,1300,res=100)
lollipopPlot2(m1=sub_1,m2=sub_2,gene=gene[2],m1_name=arg[1],m2_name=arg[2])
dev.off()
