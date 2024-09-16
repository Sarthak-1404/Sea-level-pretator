import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color='blue')

res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

years_extended = pd.Series(range(1880, 2051))
sea_level_extended = res.intercept + res.slope * years_extended

plt.plot(years_extended, sea_level_extended, color='red', label='Best fit line (1880-2050)', linestyle='-', linewidth=2)

df_recent = df[df['Year'] >= 2000]
res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

years_recent = pd.Series(range(2000, 2051))
sea_level_recent = res_recent.intercept + res_recent.slope * years_recent

plt.plot(years_recent, sea_level_recent, color='green', label='Best fit line (2000-2050)', linestyle='--', linewidth=2)

plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')

plt.legend()

plt.savefig('sea_level_plot.png')
plt.show()
