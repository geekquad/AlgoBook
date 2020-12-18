# Linear Discriminant Analysis

## Preprocessing

The notebook first reads the wine dataset which has three class labels and 13 features.

The wine data is split into training set and test set in a ratio of 7/3 using the train_test_split in sklearn.model_selection.

The training set in now standarised using using sklearn.preprocessing.


## Mean vectors

Mean vectors in the mean value of all the features for each class label. There are three class labels in this dataset. The mean vectors are calculated and stored in a list, mean_vecs.

## within-class scatter matrix and Between-class matrix

The between-class and within-class scatter matrix using the numpy matrices and using the numpy.cov to compute the covariance matrices.

## Eigen paires
The eigen pairs for the matrix S_W^(-1)*S_B is calculated using the numpy.linalg.eig and then sorted in descending order wrt the the eigen values. A list of (eigenvalue, eigenvector) tuples is generated to be sorted in descending order so that we can select the required number of features with most variance.

## Explained variance

Explained variance is variance of one feature / sum of all the variances. It is computed and represented using matplotlib

## Sorting Eigon pairs and Transformation matrix

We select only two most important features.
Using numpy.hstack we form a transformation matrix. Now, training data (X_train_std) with d features (13 in the example) is transformed to 2 feature dataset.

# Using Scikit learn

We now use the builtin LinearDiscriminantAnalysis in the scikit learn.
Logistic regression model is used to compare decision region of training set and test set. 
n_component parameter defines the number of features to choose from the training set.