import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Function to add borders to plots
def formatplot(ax, color):
    """Adds formatted border to plots."""
    for spine in ax.spines.values():
        spine.set_edgecolor(color)
        spine.set_linewidth(2)
    ax.tick_params(direction='in', length=6, width=2)

# Read all the data files to get data
df_fertilizer = pd.read_csv('FertilizerConsumption.csv').nlargest(10, '2020')
df_co2 = pd.read_csv('Co2Emissions.csv')
df_crop = pd.read_csv('CropIndex.csv')
df_agri = pd.read_csv('Agriland.csv')

# Define colors for the pie charts
colors = ['#ff9999', '#66b3ff']

# Create a figure and define the grid
fig = plt.figure(figsize=(18, 24))
gs = GridSpec(5, 2, figure=fig, height_ratios=[4, 4, 4, 1, 0.2])

Heading = fig.suptitle(
    "Analysis on Agricultural Productivity and Environmental Impact",
    fontsize=30, color='brown', fontweight='bold')

# Line Plot for Crop Production Index
ax1 = fig.add_subplot(gs[0, :])
ctry_codes = df_crop['Region']
years = df_crop.columns[2:]
for idx, code in enumerate(ctry_codes):
    ax1.plot(years, df_crop.iloc[idx, 2:], label=code)
ax1.set_title('Crop Production Index (1970-2020)', fontweight='bold',
              fontsize=18, color='darkgreen', pad=20)
ax1.set_ylabel('Crop Index', fontweight='bold', fontsize=18)
ax1.set_xlabel('Year', fontweight='bold', fontsize=18)
ax1.legend()
formatplot(ax1, 'black')
ax1.tick_params(axis='x', labelsize=12, labelrotation=0)

# Bar Chart for CO2 Emissions
ax3 = fig.add_subplot(gs[1, 0])
pos = list(range(len(df_co2['Region'])))
width = 0.4
ax3.bar(pos, df_co2['1990'], width, label='1990', color='darkblue')
ax3.bar([p + width for p in pos], df_co2['2020'], width,
        label='2020', color='pink')
ax3.set_xticks([p + width / 2 for p in pos])
ax3.set_xticklabels(df_co2['Region'], rotation=30)
ax3.set_ylabel('CO2 Emissions (kt)', fontweight='bold', fontsize=18)
ax3.set_xlabel('Regions', fontweight='bold', fontsize=20)
ax3.set_title('CO2 Emissions by Region: 1990 vs. 2020', fontweight='bold',
              fontsize=18, color='darkgreen', pad=20)
ax3.legend()
formatplot(ax3, 'black')

# Pie Chart for Agricultural Land
ax_pie = fig.add_subplot(gs[1, 1])
year = '2020'
agri_land = df_agri[year][0]
othr_land = 100 - agri_land
ax_pie.pie([agri_land, othr_land],
           labels=['Agricultural Land', 'Other Land'], colors=colors,
           autopct=lambda p: f'{p:.1f}%' if p > 0 else '',
           startangle=90, pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax_pie.add_artist(centre_circle)
ax_pie.set_title(f'Agricultural Land in {year} (% of Land Area)',
                 fontweight='bold', fontsize=18, color='darkgreen', pad=20)
formatplot(ax_pie, 'black')
plt.draw()
for text in ax_pie.texts:
    text.set_fontsize(14)

# Horizontal Bar Chart for Fertilizer Consumption
ax2 = fig.add_subplot(gs[2, :])
ctrs = df_fertilizer['Country Name'].tolist()
cons = df_fertilizer['2020'].tolist()
ax2.barh(ctrs, cons, color='skyblue', linewidth=2)
ax2.set_xlabel('Fertilizer Consumption (kg/ha of arable land)',
               fontweight='bold', fontsize=18)
ax2.set_ylabel('Countries', fontweight='bold', fontsize=18)
ax2.set_title('Top 10 Countries by Fertilizer Consumption in 2020',
              fontweight='bold', fontsize=18, color='darkgreen', pad=20)
ax2.grid(axis='x', linestyle='--', alpha=0.7)
ax2.set_xlim(0, max(cons) * 1.1)
for tick in ax2.get_yticklabels():
    tick.set_fontweight('bold')
    tick.set_fontsize('14')
for i, value in enumerate(cons):
    ax2.text(value, i, f' {value}', va='center', fontsize=12,
             fontweight='bold', color='darkgreen')
ax2.tick_params(axis='y', labelsize=12, labelrotation=0)

# Text Block for Annotations
textblock = plt.subplot(gs[3, :])
textblock.axis('off')
txtcontent = (
    "- Crop production index potentially increased by 50% \n over 50 years,"
    " linked to fertilizer use.\n"
    "- CO2 emissions in agricultural regions, like East Asia & Pacific,\n"
    " may have risen by 25% since 1990.\n"
    "- Agriculture occupies 38.57% of land, impacting the environment significantly.\n"
    "- Some countries show fertilizer usage exceeding 1000 kg/ha,"
    " reflecting intensive agriculture.\n"
    "- The trade-off between higher yields and increased emissions highlights"
    " the need for sustainable farming methods."
)
textblock.text(0, 0.5, txtcontent,
             ha='left', va='center', fontsize=25, color='black', wrap=True)

# Name and ID Block
dtls = plt.subplot(gs[4, :])
dtls.axis('off')
dtls.text(0.95, 0.5, "Name:Rajani Boddupally \n ID:22096649 ", ha="right",
                fontsize=18, color='black')

# Set the background color for the figure
fig.patch.set_facecolor('#F5F5F5')

# Adjust space between plots
fig.subplots_adjust(wspace=0.2, hspace=1)
plt.show()