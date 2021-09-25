## Backorder Detection
A backorder is an order for a good or service that cannot be filled at the current time due to a lack of available supply. The item may not be held in the company's available inventory but could still be in production, or the company may need to still manufacture more of the product.

**Problem definition**
A machine learning model to predict if a product will be in backorder or not.

### Architecture on Amazon web services
![model-aws](https://user-images.githubusercontent.com/74520811/131646698-4d8b1bf6-f621-46ef-a96c-0a45ce11c32a.png)

### Scores
* Accuracy score: 65
* Precission score: 67
* Recall score: 54
* F1 score: 60

### Algorithms used
* Artificial Neural Network
* RandomForestClassifier
* DecisionTree
* NaiveBayes
* LogisticRegression
* K-Nearest Neighbour(KNN)
* Support Vector Machine(SVM)
* GradientBoostingClassifier

### Evaluation Metrics used
* Accuracy score
* F1 score
* Precision
* Recall
* Confusion matrics
* Classification report

### GCP Services used
* CloudRun
* Container Registory
* Cloud Storage Bucket


### Deployment on GCP
The model was deployed on Google Cloud Platform.

### Steps:
* Create a GCP account.
* Create a new project or you can decide to use the default project.
* Give permission to execute the script file by running the commad `chmod +x script.sh`
* Run the script to dploy the resources `./script`.
* After successfully deployment, A url will be displayed. Place the url in your browser and follower the instructions to get started.

**Note:** Before you run this script open the file and change the values for the variable names. You can leave everything to use the default values but you must change the `Project ID` with the name of your project ID.

