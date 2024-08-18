import os
import numpy as np
import matplotlib.pyplot as plt

scripts = [file for file in os.listdir() if file[-3:] == ".py" and file != "create_plot.py"]

_fig = plt.gcf()
initial_figsize = _fig.get_size_inches()

for file_name in scripts:
    plt.figure(figsize = initial_figsize)
    plt.clf()
    print("Exec'ing " + file_name + "...")
    with open(file_name) as script:
        exec(script.read())

# plt.clf()
# exec(open("yetAnotherDiscreteTimeSignal.py").read())
