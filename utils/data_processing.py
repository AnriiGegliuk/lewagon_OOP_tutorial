import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler

class BasicMLPipline:
    # initializing your model and establishing atributes
    def __init__(self, df, target_column, model, metrics, feature_columns=None):
        self.df = df
        self.target_column = target_column
        self.model = model
        self.metrics = metrics
        if feature_columns:
            self.feature_columns = feature_columns
        else:
            self.feature_columns = [col for col in df.columns if col != target_column]

    # def missing_values_info(self):
    #     missing_data = self.df.isnull().sum()
    #     total_data = len(self.df)
    #     missing_percentage = (missing_data / total_data) * 100
    #     return missing_percentage

    def missing_val(self):
        return (self.df.isnull().sum() / len(self.df)) * 100

    def clean_data(self, columns_to_drop=None):
        self.df.dropna(inplace=True)
        if columns_to_drop:
            self.df.drop(columns=columns_to_drop, inplace=True)

    def scale_features(self, columns_to_scale):
        scaler = StandardScaler()
        self.df[columns_to_scale] = scaler.fit_transform(self.df[columns_to_scale])

    def class_distribution(self):
        return self.df[self.target_column].value_counts()


    def evaluate_model(self):
        X = self.df[self.feature_columns]
        y = self.df[self.target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        results = {}
        for metric in self.metrics:
            if metric == 'accuracy':
                results['accuracy'] = accuracy_score(y_test, y_pred)
            elif metric == 'precision':
                results['precision'] = precision_score(y_test, y_pred)
            elif metric == 'recall':
                results['recall'] = recall_score(y_test, y_pred)
            elif metric == 'f1':
                results['f1'] = f1_score(y_test, y_pred)
            elif metric == 'roc_auc':
                results['roc_auc'] = roc_auc_score(y_test, y_pred)

        return results
