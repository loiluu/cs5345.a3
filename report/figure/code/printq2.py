__author__ = 'loi'
import ast
with open("inlist.data", 'r') as f:
    in_list = ast.literal_eval(f.read())

with open("outlist.data", 'r') as f:
    out_list = ast.literal_eval(f.read())

import matplotlib.pyplot as plt
import numpy

plt.hist(in_list, bins=30, alpha=0.5, log=True, label='Same ORG')
plt.hist(out_list, bins=30, alpha=0.5, log=True, label='Diff ORG')
plt.title("Distance histogram")
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.legend()
plt.show()
