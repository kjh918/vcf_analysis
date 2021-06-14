library(ggplot2)

file_list <- list.files(paste0(getwd(),'/sample_data'))
print(file_list)
for (i in file_list){
	sample <- read.table(file=paste0(getwd(),'/sample_result/',i),header=T,sep='\t',stringsAsFactors = FALSE)
	total <- sample$total
	rownames(sample) <- as.vector(sample[,1])
	sample_new <- sample[,c(2:as.numeric(NROW(colnames(sample))-3))]
	sample <- sample_new[,!(names(sample_new) %in% 'total')]
	name <- substr(i,1,nchar(i)-3)
	sample <- t(sample)
	png(paste0(getwd(),'/plot_',name,'png'),width=2000,height=1300,res=150)
	bar = barplot(as.matrix(sample),col=rainbow(8),names.arg=colnames(sample),cex.names=0.7,angle=90,las=2,ylim=c(0,30))
	legend('topright',legend=rownames(sample),cex=0.7,fill=rainbow(8))
	text(x=bar,y=as.vector(total),labels=as.vector(total),pos=3,cex=0.7)
	dev.off()

}
