from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import sklearn as sk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Classification:
    def __init__(self, csv_file_path, feature_variables, prediction_data, should_plot_data=False):
        self.csv_file_path = csv_file_path
        self.features = feature_variables

        self.model = None

        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        self.prediction_data = prediction_data
        self.should_plot_data = should_plot_data

        self.get_and_split_data()

    def start(self):
        """
        This will perform the training, testing, and prediction tests on the model
        """
        self.train()
        self.test()
        self.predict()

    def get_and_split_data(self):
        data = pd.read_csv(self.csv_file_path)
        data = data.dropna()

        label_encoder = LabelEncoder()
        data.insert(1, "Type 2 Classes", label_encoder.fit_transform(
            data["ocean_proximity"]), True)

        X = data[self.features]
        y = data["Type 2 Classes"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=0)

        self.__plot_data(self.X_train, self.y_train, "b")
        self.__plot_data(self.X_test, self.y_test, "r")

    def __plot_data(self, X, y, color):
        """
        Plot data ONLY IF the independent variable, X, has a shape of (some length, 1) which means it only
        has 1 feature (eg. [["Attack"]] would be fine but [["Attack", "Defense"]] would not be)
        """
        if X.shape[1] == 1 and self.should_plot_data:
            plt.scatter(X, y, c=color)

    def train(self):
        """
        Train the model using Scikit Learn's LinearRegressionModel()
        """
        self.model = DecisionTreeClassifier().fit(self.X_train, self.y_train)

    def test(self):
        """
        Test the model using the testing dataset that was made when first creating the data, and then output the score
        and RSME (Root Mean Square Error)
        """
        y_pred = self.model.predict(self.X_test)
        y_true = np.array(self.y_test)[
            len(self.y_test) - len(y_pred):]
        matches = []
        number_of_trues = 0
        number_of_falses = 0
        for i, item in enumerate(y_pred):
            if item == y_true[i]:
                matches.append(True)
                number_of_trues += 1
            else:
                matches.append(False)
                number_of_falses += 1

        print(f"Number of matches: {number_of_trues}")
        print(f"Number of incorrect answers: {number_of_falses}")
        print(f"Accuracy Score: {accuracy_score(
            y_true=y_true, y_pred=y_pred)}")
        print(f"F1 Score: {f1_score(y_true=y_true,
              y_pred=y_pred, average="micro")}")

    def predict(self):
        """
        Predict new values based on the new data given and print out the score and RSME
        """
        y_pred = self.model.predict(self.prediction_data)

        print(f"Prediction data: {self.prediction_data[0][0]}")
        print(f"y prediction: {round(y_pred[0])}")


print("\n/////////////////////////////////////////////////////////////////////\n")

model_1 = Classification(
    csv_file_path="MachineLearning/housing.csv",
    feature_variables=["median_house_value"],
    prediction_data=[[452600.0]])

model_1.start()

print("\n/////////////////////////////////////////////////////////////////////\n")
