
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class Splits:

  def __init__(self, df):

    """
    Constructor for train, validate, test split
    Splits target vector of df from feature matrix
    Then splits into the above 3 sets.
    """
    # Attributes
    self.y = df[df.columns[-1]]
    self.X = df.drop(df.columns[-1], axis=1)

  # Methods
  def multi_split(self):
    """Makes train, val, and test sets out of a dataframe """
    
    # split the target vector from the feature matrix
    X_train, X_val, y_train, y_val = train_test_split(self.X, self.y, 
                                                      test_size=0.3, 
                                                      random_state=42)

    # Split validation group further into validation and test groups
    X_val = X_val.reset_index(drop=True)
    X_test = X_val.loc[(.3 * self.X.shape[0]//2) + 1:]
    X_val = X_val.loc[0:(.3 * self.X.shape[0])//2]

    # Establish validation labels corresponding to validation features
    y_val = y_val.reset_index(drop=True)
    y_test = y_val.loc[(.3 * self.X.shape[0]//2) + 1:]
    y_val = y_val.loc[0:(.3 * self.X.shape[0])//2]

    # Print the shapes of these new datasets
    print('X_train:', X_train.shape)
    print('y_train:', y_train.shape)
    print('X_val:', X_val.shape)
    print('y_val:', y_val.shape)
    print('X_test:', X_test.shape)
    print('y_test:', y_test.shape)

    # Return the six new data sets

    self.X_train = X_train

    return X_train, y_train, X_val, y_val, X_test, y_test