

import numpy as np
import pandas as pd
import sys

sys.___stdout__=sys.stdout

# iterated over keys and values in a loop (page 77)

df = pd.DataFrame(np.random.randn(4,3),columns=['A','B','C'])

for key,value in df.iteritems():
  
  # additional edits
