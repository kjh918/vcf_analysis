library('ggplot2')
library('maftools')

data<-read.maf(maf='~/kjh/Num_maf/52.maf')

t_vaf <- as.numeric(data@data$t_alt_count)/as.numeric(data@data$t_depth)
data@data <- cbind(data@data, t_vaf)

t_vaf <- as.numeric(data@maf.silent$t_alt_count)/as.numeric(data@maf.silent$t_depth)
data@maf.silent <- cbind(data@maf.silent, t_vaf)

sub = subsetMaf(maf=data, query='t_depth >= 500')
sub = subsetMaf(maf=sub, query='t_vaf >= 0.01')

## Sample Varidation Count
# getSampleSummary(sub)

## Gene Varidation Count
# getGenesSummary(sub)

## Samples + Genes 
# mafSummary(sub)

# summary plot

png('~/kjh/png/plotsummary.png',1300,1300,res=150)
plotmafSummary(sub, showBarcodes=TRUE,addStat='mean',top=15)
dev.off()

# Mafdata Header information
# getField(sub)

# save maf data 
write.mafSummary(sub,basename='~/kjh/mafSummary/mafSummary.txt')

# save score to text
# score based on intra-tumor genetic heterogeneity
# mat.socre(sub)
# oncoplot 
png('~/kjh/png/oncoplot.png',800,800,res=100)
oncoplot(sub,showTumorSampleBarcodes=TRUE,draw_titv=TRUE)
dev.off()

# lollipopPlot
png('~/kjh/png/lolliplot.png',800,800,res=95)
lollipopPlot(maf=sub, gene='TP53', repel=TRUE, labelPos="all", labPosAngle=45)
dev.off()

# plotTiTv
# SNP sort Transition Transversion -> boxplot
print('plotTiTV')
png('~/kjh/png/plotTitv.png',800,800,res=100)
sub.titv = titv(maf=sub, plot=FALSE, useSyn=FALSE)
plotTiTv(res=sub.titv, showBarcodes=TRUE)
dev.off()

# PlotVaf
# most Varidation count Variant allele frequency -> boxplot
png('~/kjh/png/plotVaf.png',800,800,res=100)
plotVaf(sub,top=20, keepGeneOrder=TRUE)
dev.off()

# TCGACompare
# Mutation burden check
png('~/kjh/png/tcgaCompare.png',800,800,res=100)
tcgaCompare(maf=sub,cohortName='PemVim')
dev.off()

# SomaticInteractions
png('~/kjh/png/somaticInteraction.png',800,800,res=100)
somaticInteractions(maf=sub)
dev.off()

# oncodrive / plotOncodirve
# driver cancer gene 
png('~/kjh/png/oncodrive.png',800,800,res=70)
hotspot = oncodrive(maf=sub, pvalMethod = 'zscore')
print(hotspot)
plotOncodrive(res=hotspot)
dev.off()

