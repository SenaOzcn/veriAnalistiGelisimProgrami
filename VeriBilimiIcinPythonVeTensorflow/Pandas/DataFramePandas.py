import numpy as np
import pandas as pd

data = np.random.randn(4,3)
data
## array([[ 0.46484375,  0.28128691,  0.9473642 ],
##        [ 1.12678968, -0.25719882,  1.15687883],
##        [ 2.04686066,  0.13855855, -0.0891846 ],
##        [ 0.3786098 , -1.38290678,  0.1392032 ]])

dataFrame = pd.DataFrame(data)
## 	     0	            1	          2
## 0	0.464844	0.281287	0.947364
## 1	1.126790	-0.257199	1.156879
## 2	2.046861	0.138559	-0.089185
## 3	0.378610	-1.382907	0.139203

dataFrame[0]
## 0    0.464844
## 1    1.126790
## 2    2.046861
## 3    0.378610
## Name: 0, dtype: float64

newDataFrame = pd.DataFrame(data, index=["Atıl", "Zeynep", "Atlas", "Mehmet"], columns=["Salary", "Age", "Working Hours"] )
newDataFrame
##	         Salary	           Age	    Working Hours
## Atıl	        0.464844	0.281287	0.947364
## Zeynep	1.126790	-0.257199	1.156879
## Atlas	2.046861	0.138559	-0.089185
## Mehmet	0.378610	-1.382907	0.139203

