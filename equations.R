import pandas as pd
import numpy as np
#mean
mean = mean(IBM_Marks1$Total)
print(mean)

install.packages("modeest")
library(modeest)
mlv(IBM_Marks1$`MTE (25)`, method = "mfv")

#get the median of variable MTE
median(IBM_Marks1$`MTE (25)`)

#quantile
d <- c(3,4,7,8,5)
print(d)
quantile(d,c(0.50))

d <- c(3,4,7,8,5)
print(d)
quantile(d,c(0.75))

d <- c(3,4,7,8,5)
print(d)
quantile(d,c(0.25))


#minmax
min(d)
max(d)

#range
range(d)
print(max(d)-min(d))

#mode
mode function(){
  return(sort(-table(IBM_Marks1$`MTE (25)`)))
}
mode()

#variance
var(IBM_Marks1$Total)

#inter quantile range
IQR(d)

#standard devitation
sd(IBM_Marks1$`Total (50)`)

#boxplot
boxplot(IBM_Marks1$Total)

boxplot(IBM_Marks1$Total,horizontal = TRUE)

#scatterplot
install.packages("scatterplot3d")
library(scatterplot3d)
attach(IBM_Marks1)
scatterplot3d(Total,ETE(50),main="scatter_plot,xlab="Total",ylab="ETE(50)",zlab="MTE(50",pch=18))
