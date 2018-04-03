import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Dataset
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
 
# plot
df.plot.area()
