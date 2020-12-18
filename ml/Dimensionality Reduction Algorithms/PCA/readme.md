# Principal Component Analysis

## Preprocessing

The notebook first reads the wine dataset which has three class labels and 13 features.

The wine data is split into training set and test set in a ratio of 7/3 using the train_test_split in sklearn.model_selection.

The training set in now standarised using using sklearn.preprocessing.


## Eigen values
Using the cov method of numpy covariance matrix in computed.Now, numpy.linalg.eig is used to compute the eigen_vals and eigen vecs

## Explained variance

Explained variance is variance of one feature / sum of all the variances. It is computed and represented using matplotlib

## Sorting Eigon pairs and Transformation matrix

A list of (eigenvalue, eigenvector) tuples is generated to be sorted in descending order so that we can select the required number of features with most variance.
We select only two features which accounts for about 60% of variance for representation purpose.
Using numpy.hstack we choose two eigen paris and form a transformation matrix.

## New dataset

New dataset X_train_pca is computed by matrix multiplication of X_train_std and the transformation matrix (w). And then the new dataset is plotted using matplotlib.


# Using scikit learn builit PCA

We now use the builtin PCA in the scikit learn.

Logistic regression model is used to compare decision region of training set and test set. 
n_component parameter defines the number of features to choose from the training set.

When n_components is given as none the PCA class choose all the features and we can get the explained_variance-ratio