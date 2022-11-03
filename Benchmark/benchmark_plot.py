from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ticks = ('Example 1', 'Example 2', 'Example 3', 'Example 4')
twinson_average_mean = [2.2, 4.7, 11.4, 41.6]
domparser_average_mean = [4.2, 7.0, 12.0, 42.1]
twinson_average_err = [1.4, 2.4, 5.5, 17.2]
domparser_average_err = [2.5, 3.5, 9.4, 17.0]

y_pos = np.arange(len(ticks))
y_pos1 = y_pos - 0.175
y_pos2 = y_pos + 0.175
height = 0.35

plt.figure(figsize=(9.0, 4.0), dpi=120)

# Average
plt.subplot(1, 1, 1)
plt.suptitle("""Direct-Element-Access benchmark of Twinson JSON decoder for examples with increasing complexity.
All elements are accessed directly (no node caching for arrays). Averaged over 5000 iterations.
VM with TwinCAT 3.1.4024.35; AMD Ryzen 3600X (1 Isolated Core)""", fontsize=10)

ax = plt.gca()
ax.grid(True, linestyle='--', color='grey', alpha=.25)
ax.barh(y_pos1, twinson_average_mean, height=height, xerr=twinson_average_err, label='Twinson')
ax.barh(y_pos2, domparser_average_mean, height=height, xerr=domparser_average_err, label='Tc3_Json')
ax.set_yticks(y_pos)
ax.set_yticklabels(ticks)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Mean Calculation Duration [µs]')
ax.legend()

plt.savefig(Path(__file__).parent.parent / 'benchmark.png')
