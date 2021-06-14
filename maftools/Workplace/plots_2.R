library('ggplot2')
library('maftools')
a = '~/kjh/abc'
file_list <- list.files(a)

for (i in file_list){
	print('#####################a#############################')
	print(paste0(i,' starting'))
	print('##################################################')
	data <- read.maf(maf=paste(a,'/',i,sep=''))
	sub <- data
	dir.create(paste('~/kjh/maf_result/',i,sep=''))
	# Sample Analysis data
	write.mafSummary(sub,basename=paste('~/kjh/maf_result/',i,'/',i,sep=''))
	
	# Summary Plot
	png(paste0('~/kjh/maf_result/',i,'/plotsummary.png'),1300,1300,res=150)
	plotmafSummary(sub, showBarcodes=TRUE,addStat='mean',top=15)
	dev.off()

	# oncoplot

	png(paste0('~/kjh/maf_result/',i,'/oncoplot.png'),1300,1300,res=150)
	oncoplot(sub,showTumorSampleBarcodes=TRUE,draw_titv=TRUE)
	dev.off()

	# lollipopPlot

	png(paste0('~/kjh/maf_result/',i,'/lollipopPlot.png'),1300,1300,res=150)
	lollipopPlot(maf=sub, gene='TP53', repel=TRUE, labelPos="all", labPosAngle=45)
	dev.off()

	# plotTiTv
	# SNP sort Transition Transversion -> boxplot
	png(paste0('~/kjh/maf_result/',i,'/plotTiTv.png'),1300,1300,res=150)
	sub.titv = titv(maf=sub, plot=FALSE, useSyn=FALSE)
	plotTiTv(res=sub.titv, showBarcodes=TRUE)
	dev.off()

	# PlotVaf
	# most Varidation count Variant allele frequency -> boxplot
	png(paste0('~/kjh/maf_result/',i,'/plotVaf.png'),1300,1300,res=150)
	plotVaf(sub,top=20, keepGeneOrder=TRUE)
	dev.off()


	# TCGACompare
	# Mutation burden check
	png(paste0('~/kjh/maf_result/',i,'/tcgaCompare.png'),1300,1300,res=150)
	tcgaCompare(maf=sub,cohortName='PemVim')
	dev.off()

	# SomaticInteractions
	png(paste0('~/kjh/maf_result/',i,'/somaticInteractions.png'),1300,1300,res=150)
	somaticInteractions(maf=sub)
	dev.off()
	
	try({
	# oncodrive / plotOncodrive
	# driver cancer gene 
		png(paste0('~/kjh/maf_result/',i,'/plotOncodrive.png'),1300,1300,res=150)
		hotspot = oncodrive(maf=sub, pvalMethod = 'zscore')
		plotOncodrive(res=hotspot)
		dev.off()
	}, silent = T)
	print(paste0(i,' finished'))

}




