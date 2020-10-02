import pandas as pd
import numpy as np
from scipy import stats


class Chi2:

   def __init__(self, x1, x2):
      """
      Constructor for Chi2 reporting module
      Takes two categorical variable Series
      Returns Chi2 test info and contingency table
      """
      # Attributes
      self.x1 = x1.apply(lambda x: str(x))
      self.x2 = x2.apply(lambda x: str(x))

   def chi2_report(self):
      contingency = pd.crosstab(self.x1, self.x2)

      chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

      print("chi2:", chi2)
      print("p value:", p_value)
      print("dof:", dof)
      print("expected_frequencies: \n", expected)
      print("Contingency Table:", contingency)
