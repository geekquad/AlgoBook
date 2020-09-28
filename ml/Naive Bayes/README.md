# Naive Bayes Algorithm

**This markdown file is to give you a detailed and easy-to-understand explaination of WHAT the famous Naive Bayes algorithm is and WHY it is used widely in the field of machine learning.
Read the file to the end for better understanding.**

**Go through the Jupyter Notebook to learn how the algorithm is implemented and how it is used to solve machine learning problems.**

**For and doubts and queries, create an issue. :smile:**

<img src="https://miro.medium.com/max/640/1*7lg_uLm8_1fYGjxPbTrQFQ.png">
Formula for Gaussain Naive Bayes.
<hr> </hr>

## What is Naive Bayes :question:

* Naive Bayes is a probability based machine learning algorithm that is used for large volumes of data.
* It gives very good results when it comes to NLP tasks such as sentimental analysis. 
* It is a fast and uncomplicated classification algorithm.
* It is based on the *Bayes Theorem* with an assumption of independence among predictors.

## What are it's applications :closed_book:?

* **Real Time Prediction:** As Naive Bayes has low Time Complexity, it can be easily deployed and used for real time applications.
* **Multi-Class Prediction:** The algorithm can be used in multi-class prediction scenario as it can predict the posterior probability of mulltiple classes of the target variable.
* **Natural Language Processing:** Because of their good performance in multi-class settings, Naive Bayes tends to be very useful in  NLP applications like:
    * Text Classification
    * Spam Filtering
    * Sentiment Analysis, etc.
* **Recommendation Systems:** It helps in recommendation system because of probabilistic prediction ability and low time complexity.

## Types of Naive Bayes Algorithms:file_folder::

* **Gaussian Naive Bayes:** 
    * Used in Classification
    * Assumes that features follow normal distribution
* **Multinomial Naive Bayes:**     
    * Suitable for classification with discrete features, e.g., word count for text classification.
* **Bernoulli Naive Bayes:**    
    * Used for data that is distributed according to multivariate Bernoulli distributions.
    * Features should be independent booleans.
    
## Why is Naive Bayes so naive :open_mouth:?

* Naive Bayes (NB) is ‘naive’ because it makes the assumption that features of a measurement are independent of each other.

## Pros and Cons of Naive Bayes:
### Pros :white_check_mark::

* Highly extensible and fast algorithm , Time Complexity:O(nK), where n is the number of features and K is the number of class lables.
* Performs well in both binary and  multi-class settings.
* When assumption of independence holds, a Naive Bayes classifier performs better compare to other models like logistic regression and you need less training data.
* Performs well whin data is categorical or normally distributed.
* Can be easily trained on small datasets and can be used for large ones as well.

### Cons :x::

* The main disadvantage of the NB is considering all the variables independent that contributes to the probability. 
* If categorical variable has a category (in test data set), which was not observed in training data set, then model will assign a 0 (zero) probability and will be unable to make a prediction. This is often known as “Zero Frequency”. To solve this, we can use the smoothing techniques like Laplace or Additive smoothing.

### Documentation of GaussianNB:
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html"> https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html </a>

<hr> </hr>

### Dataset Used: Wine Quality Dataset
### Problem Type: Multi-Class Classification
### Algorithm Used: Gaussian Naive Bayes
### Evaluation of the Model:
            precision    recall  f1-score   support
      0       0.91      0.95      0.93        21
      1       0.94      0.79      0.86        19
      2       0.88      1.00      0.93        14

    avg / total   0.91      0.91      0.91        54
### Accuracy: 90.7 % 
