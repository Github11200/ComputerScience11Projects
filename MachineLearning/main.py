from sklearn import metrics
from sklearn.linear_model import LinearRegression as LinearRegressionModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    """
    This class is an abstraction on top of the linear regression model provided by Scikit Learn, and will automatically
    prepare and split the data, train, test, and finally predict on data of your choice. It will also provide information
    about the accuracy of the model and how much of a relation there is between the independent and dependent variables
    """

    def __init__(self, csv_file_path, independent_variables, dependent_variable):
        """
        Prepare all of the variables that other methods inside the class will require
        """
        self.csv_file_path = csv_file_path
        self.independent_variables = independent_variables
        self.dependent_variable = dependent_variable

        self.model = None

        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

        self.get_and_split_data()

    def get_and_split_data(self):
        """
        Read the csv file from the path provided, remove the rows with NaN in them, get the independent
        and dependent variables, and then split them into training and testing datasets
        """
        data = pd.read_csv(self.csv_file_path)
        data = data.dropna()

        X = data[self.independent_variables]
        y = data[self.dependent_variable]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.1, random_state=0)

        self.__plot_data(self.X_train, self.y_train, "b")
        self.__plot_data(self.X_test, self.y_test, "r")

    def __plot_data(self, X, y, color):
        """
        Plot data ONLY IF the independent variable, X, has a shape of (some length, 1) which means it only
        has 1 feature (eg. [["Attack"]] would be fine but [["Attack", "Defense"]] would not be)
        """
        if X.shape[1] == 1:
            plt.scatter(X, y, c=color)

    def train(self):
        """
        Train the model using Scikit Learn's LinearRegressionModel()
        """
        self.model = LinearRegressionModel().fit(
            self.X_train.values, self.y_train.values)

    def test(self):
        """
        Test the model using the testing dataset that was made when first creating the data, and then output the score
        and RSME (Root Mean Square Error)
        """
        y_pred = self.model.predict(self.X_test.values)

        print(f"Score: {self.model.score(
            self.X_test.values, self.y_test.values)}")
        print(
            f"Root mean squared error: {np.sqrt(metrics.mean_absolute_error(self.y_test, y_pred))}")

        plt.show()

    def predict(self, X):
        """
        Predict new values based on the new data given and print out the score and RSME
        """
        y_pred = self.model.predict(X)

        print(f"y prediction: {round(y_pred[0])}")


model_1 = LinearRegression(
    "MachineLearning/Pokemon.csv", ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], "Total")

model_1.train()
model_1.test()
model_1.predict([[45, 49, 49, 65, 65, 45]])

model_2 = LinearRegression(
    "MachineLearning/Pokemon.csv", ["Sp. Def"], "Sp. Atk")

model_2.train()
model_2.test()
model_2.predict([[65]])

model_3 = LinearRegression(
    "MachineLearning/Pokemon.csv", ["Defense"], "Attack")

model_3.train()
model_3.test()
model_3.predict([[49]])
