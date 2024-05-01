try:
    import pandas as pd
except ImportError:
    print("pandas module not installed")

print(pd)

import pandas as pd
df = pd.read_csv('india-data-sample.csv', index_col=0)


df.plot.scatter('Female Literacy (%)', 'Fertility Rate')


df.loc[df['Population Density (km-2)'].idxmax()]
#Out[x]: 
#Male Population              8887326
#Female Population            7800615
#Area (km2)                   1484
#Male Literacy (%)            91.03
#Female Literacy (%)          80.93
#Population                   16687940
#Population Density (km-2)    1.124524e+04
#Name: Delhi, dtype: float64


