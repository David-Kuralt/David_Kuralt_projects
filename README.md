# David_Kuralt_projects
## Some projects from my data science classes at the University of Denver
### Assignment 7 from Data Science Tools 2 class wth files ChanningHouse.csv and prostateSurvival.csv
In this assignment, we are directed to choose two datasets on our own and perform specific tasks with them. I downloaded ChanningHouse.csv and prostateSurvival.csv from [https://vincentarelbundock.github.io/Rdatasets/articles/data.html](https://vincentarelbundock.github.io/Rdatasets/articles/data.html). With ChanningHouse.csv, I apply Principal Component Analysis (PCA) to reduce the dimensionality of the dataset from four dimensions to two. Then I apply agglomerative clustering and KMeans clustering. To determine the optimal number of clusters, I plot a dendrogram, and make an elbow plot for KMeans. I conclude that the optimal number of clusters is two. Then I train a logistic regression classifier from *sklearn.linear_model* on a portion of the data. The overall accuracy of the classifier is very high on both the training and test portions of the data.

For prostateSurvival.csv, I use the multinomial logit model from *statsmodels.api* to classify data instances into one of three possible categories: those subjects with prostate cancer who survived throughout time period the study, those who died from prostate cancer during the study, and those who died from other causes during the study. The emphasis on this part of the assignment is to interpret the model coefficients and to comment on their statistical significance. The accuracy of my model is similar on both the training and test portions of the data, which means that overfitting the training data is not an issue. However, it is a poor model overall because it fails to predict any of the death outcomes correctly. The number of subjects who survived the course of the study is proportionally much greater than the number of subjects who did not.
