#15/08/2022 
#juliomoreno7217@gmail.com

2+5
#Comments

print("message")

# Creating variables 
x <- 35
x <- 1
x

# Creating arrays
y <- c(1,1,1,1,1,1,1)
z <-1:5

# Two variables at once
a <- b <- 1:4

#Array's elements addition:
a+b
#Array's elements multiplication:
a*b

ls()
rm(z) #remove() is valid too

#Remove all variables: 
rm(list=ls())


#Import Packages: (in-built packages at the right subwindow)
#https://cran.r-project.org/web/views/

browseURL("https://cran.r-project.org/web/views/")

install.packages("LiblineaR")

library()
search()
#require("LiblineaR")
#detach("package:LiblineaR", unload=True)   Unload Packages

? LiblineaR  #info about the package

#In-built datasets
data()
library(help="datasets") 

#Iris dataset:

? iris
str(iris)
iris

#The dataset is now ready to use (in the workspace)
data("iris")

x <- seq(2, 20, by = 1)

y <- scan()
