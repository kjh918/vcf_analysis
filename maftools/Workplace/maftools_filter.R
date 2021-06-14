library('ggplot2')
library('maftools')

arg <- commandArgs(TRUE)
path <- paste0(getwd(),'/',arg[1])

file_list <- list.files(path)

print(NROW(file_list))

"""
for (i in file_list){
	print('#####################a#############################')
	print(paste0(i,' starting'))
	print('##################################################')
	data <- read.maf(maf=paste(path,'/',i,sep=''))
	t_vaf <- as.numeric(data@data$t_alt_count)/as.numeric(data@data$t_depth)
	data@data <- cbind(data@data, t_vaf)

	t_vaf <- as.numeric(data@maf.silent$t_alt_count)/as.numeric(data@maf.silent$t_depth)
	data@maf.silent <- cbind(data@maf.silent, t_vaf)

	sub = subsetMaf(maf=data, query='t_depth >= 500')
	sub = subsetMaf(maf=sub, query='t_vaf >= 0.01')
	dir.create(paste('~/kjh/2.filtdata/',i,sep=''))
	#write.table(sub,file=paste('~/kjh/2.Filtdata/',i,'/',sep=''),sep='\t')
	# Sample Analysis data
	write.mafSummary(sub,basename=paste('~/kjh/2.Filtdata/',i,'/',i,sep=''))

}
"""


