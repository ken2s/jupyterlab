targetPackages <- c('ISLR', 'car', 'fmsb', 'class', 'boot', 'leaps', 'glmnet', 'pls', 'splines', 'locfit', 'gam', 'akima', 'tree', 'randomForest', 'gbm', 'e1071', 'LiblineaR', 'ROCR', 'openxlsx', 'PerformanceAnalytics', 'abind', 'bitops', 'readr', 'dplyr', 'ggplot2', 'forcats', 'tidyverse', 'multcomp', 'mvtnorm', 'TH.data', 'sandwich', 'xgboost', 'kernlab') 
newPackages <- targetPackages[!(targetPackages %in% installed.packages()[,"Package"])]
if(length(newPackages)) install.packages(newPackages, repos = "https://ftp.yz.yamagata-u.ac.jp/pub/cran/")
for(package in targetPackages) library(package, character.only = T)
