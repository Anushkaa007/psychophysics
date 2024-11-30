import numpy as np
import pandas as pd

np.random.seed(0)

num_of_options = 100
half_of_options = int(num_of_options/2)

min_f = 0.2
max_f = 0.9

min_delay = 0.7
max_delay = 5.0


delays = np.random.uniform(size=num_of_options) * (max_delay-min_delay) + min_delay

f1_high = np.random.uniform(size=half_of_options) * (max_f - 0.5) + 0.5
f2_high = np.random.uniform(size=half_of_options) * (max_f - 0.5) + 0.5
f3_high = np.random.uniform(size=half_of_options) * (max_f - 0.5) + 0.5

f1_low = np.random.uniform(size=half_of_options) * (0.5 - min_f) + min_f
f2_low = np.random.uniform(size=half_of_options) * (0.5 - min_f) + min_f
f3_low = np.random.uniform(size=half_of_options) * (0.5 - min_f) + min_f

f1 = np.concatenate([f1_low, f1_high])
f2 = np.concatenate([f2_low, f2_high])
f3 = np.concatenate([f3_low, f3_high])

start1 = np.ones(num_of_options,dtype=f1.dtype)
start2 = start1 + delays
start3 = start2 + delays


D = pd.DataFrame({
	'delay'	: delays,
	'start1': start1,
	'start2': start2,
	'start3': start3,
	'f1'	: f1,
	'f2'	: f2,
	'f3' 	: f3,
	'f1_greater'	: (f1 > f2) & (f1 > f3),
	'f2_greater'	: (f2 > f1) & (f2 > f3),
	'f3_greater'	: (f3 > f2) & (f3 > f1)
})


D.to_excel('delay_disc_conditions_2pop.xlsx',index=None,float_format = '%.3f',)
