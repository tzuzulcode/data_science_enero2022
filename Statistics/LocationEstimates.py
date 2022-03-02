import numpy as np
import pandas as pd
from scipy.stats import trim_mean
import wquantiles

state = pd.read_csv("../datos.csv")

meanPopulation = state["Population"].mean()

print(meanPopulation)

trimmed_mean_population = trim_mean(state["Population"],0.2)

print(trimmed_mean_population)

medianPopulation = state["Population"].median()

print(medianPopulation)

weighted_mean = np.average(state["Murder rate"], weights=state["Population"])

print(weighted_mean)

weighted_median = wquantiles.median(state["Murder rate"],weights=state["Population"])

print(weighted_median)

