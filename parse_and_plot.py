import os
import numpy as np
from matplotlib import pyplot as plt

out_directory = "out"

from raise_to_power_array import data as input_data


results = np.zeros_like(input_data)

for input_id, input_value in enumerate(input_data):
    filename = os.path.join(out_directory, f"{input_id:03}.out")
    with open(filename) as f:
        script_output = f.read()
        result = script_output.split("Result: ")[1].split('\n')[0]
        results[input_id] = float(result)

plt.plot(input_data, results)
plt.show()
