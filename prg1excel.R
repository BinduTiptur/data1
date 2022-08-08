library(readx1)
Book1 <- read_excel("D:\bindu\dataanalytics\BOOK1.xlsx")
View(Book1)
library(readxl)
Book1 <- read_excel("D:\bindu\dataanalytics\BOOK1.xlsx")
print(Book1)

#Boxplot
boxplot(Book1_csv$Salary,horizontal = TRUE)

#scatterplot3d
install.packages("scatterplot3d")
library(scatterplot3d)
attach(Book1_csv)
scatterplot3d(Salary,Start_Date,main="scatter_plot",xlab="salary",ylab = "start_date",zlab="dept",pch=18)

