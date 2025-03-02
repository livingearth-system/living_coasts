#!/usr/bin/env python
# coding: utf-8
# %%

# ### My functions
# This notebook allows you to write functions. Export these as a python script using 'File', then 'Save and export notebook as' and then select 'Executable script'

# #### Function to generate a normalised index

# %%

### NOTE THAT A GOOD LINK FOR SELECTING COLOURS IS AT https://www.google.com/search?q=what+is+the+colour+%23FF8C00+and+RGB&oq=what+is+the+colour+%23FF8C00+and+RGB&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigAdIBCDQ5OTRqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8

import numpy as np  # Add this line
import xarray as xr

def normalised_index(a,b):
    return ((a-b)/(a+b))



import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd
import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd

def plot_level3_gain(data, cmap, norm, figsize=(12, 8), title='Level 3 - Gains'):
    """
    Plots a level 3 gain map using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No Data"],
        "#ACBC2D": [111, "Cultivated Terrestrial\n Vegetation"],
        "#0E7912": [112, "Natural Terrestrial\n Vegetation"],
        "#1EBF79": [124, "Natural Aquatic\n Vegetation"],
        "#DA5C69": [215, "Artificial Surface"],
        "#F3AB69": [216, "Natural Bare\n Surface"],
        "#1a54b9": [220, "Water"]
    }

    legend_labels = [
        "No Data",
        "Cultivated Terrestrial\n Vegetation",
        "Natural Terrestrial\n Vegetation",
        "Natural Aquatic\n Vegetation",
        "Artificial Surface",
        "Natural Bare\n Surface",
        "Water"
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd

def plot_level3_loss(data, cmap, norm, figsize=(12, 8), title='Level 3 - No Change'):
    """
    Plots a level 3 loss map using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No Data"],
        "#ACBC2D": [111, "Cultivated Terrestrial\n Vegetation"],
        "#0E7912": [112, "Natural Terrestrial\n Vegetation"],
        "#1EBF79": [124, "Natural Aquatic\n Vegetation"],
        "#DA5C69": [215, "Artificial Surface"],
        "#F3AB69": [216, "Natural Bare\n Surface"],
        "#1a54b9": [220, "Water"]
    }

    legend_labels = [
        "No Data",
        "Cultivated Terrestrial\n Vegetation",
        "Natural Terrestrial\n Vegetation",
        "Natural Aquatic\n Vegetation",
        "Artificial Surface",
        "Natural Bare\n Surface",
        "Water"
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd

def plot_level3_no_change(data, cmap, norm, figsize=(12, 8), title='Level 3 - No Change'):
    """
    Plots a level 3 no change map using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No Data"],
        "#ACBC2D": [111, "Cultivated Terrestrial\n Vegetation"],
        "#0E7912": [112, "Natural Terrestrial\n Vegetation"],
        "#1EBF79": [124, "Natural Aquatic\n Vegetation"],
        "#DA5C69": [215, "Artificial Surface"],
        "#F3AB69": [216, "Natural Bare\n Surface"],
        "#1a54b9": [220, "Water"]
    }

    legend_labels = [
        "No Data",
        "Cultivated Terrestrial\n Vegetation",
        "Natural Terrestrial\n Vegetation",
        "Natural Aquatic\n Vegetation",
        "Artificial Surface",
        "Natural Bare\n Surface",
        "Water"
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd

def plot_lifeform_changes(data, cmap, norm, figsize=(12, 8), title='Lifeform Changes'):
    """
    Plots lifeform changes using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "Remained non-vegetated"],
        "#C80000": [1, "Non-vegetated to Woody"],
        "#64006E": [2, "Non-vegetated to Herbaceous"],
        "#D2D2D2": [10, "Woody to non-vegetated"],
        "#21852C": [11, "Remained woody"],
        "#A5C8B4": [12, "Woody to herbaceous"],
        "#F0F0F0": [20, "Herbaceous to non-vegetated"],
        "#C89B64": [21, "Herbaceous to woody"],
        "#A3CA54": [22, "Remained herbaceous"]
    }

    legend_labels = [
        "Remained non-vegetated",
        "Non-vegetated to Woody",
        "Non-vegetated to Herbaceous",
        "Woody to non-vegetated",
        "Remained woody",
        "Woody to herbaceous",
        "Herbaceous to non-vegetated",
        "Herbaceous to woody",
        "Remained herbaceous"
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

def plot_canopy_cover_change(data, cmap, norm, figsize=(12, 8), title='Canopy Cover Changes'):
    """
    Plots a canopy cover change map using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.2)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0.0, "No Data - Not vegetated"],
        "#E1FF00": [16, "Not-Vegetated to 1 to 4 % cover"],
        "#99FF00": [15, "Not-Vegetated to 4 to 15 % cover"],
        "#77FF00": [13, "Not-Vegetated to 15 to 40 % cover"],
        "#55FF00": [12, "Not-Vegetated to 40 to 65 % cover"],
        "#00FF6E": [10, "Not-Vegetated to > 65 % cover"],
        "#DC7A1F": [1012, "> 65 % to (40 to 65 %) cover"],
        "#DC993B": [1013, "> 65 % to (15 to 40 %) cover"],
        "#B27C2F": [1015, "> 65 % to (4 to 15 %) cover"],
        "#F70A12": [1016, "> 65 % to (1 to 4 %) cover"],
        "#8DDF35": [1210, "(40 to 65 %) to > 65 % cover"],
        "#DFD926": [1213, "(40 to 65 %) to (15 to 40 %) cover"],
        "#BAB51F": [1215, "(40 to 65 %) to (4 to 15 %) cover"],
        "#B07D35": [1216, "(40 to 65 %) to (1 to 4 %) cover"],
        "#9DC769": [1310, "(15 to 40 %) to > 65 %) cover"],
        "#95DC3C": [1312, "(15 to 40 %) to (40 to 65 %) cover"],
        "#C7BE69": [1315, "(15 to 40 %) to (4 to 15 %) cover"],
        "#C4B97C": [1316, "(15 to 40 %) to (1 to 4 %) cover"],
        "#6CC81B": [1510, "(4 to 15 %) to > 65 % cover"],
        "#50A052": [1512, "(4 to 15 %) to (40 to 65 %) cover"],
        "#97C864": [1513, "(4 to 15 %) to (15 to 40 %) cover"],
        "#C87156": [1516, "(4 to 15 %) to 1 to 4 % cover"],
        "#0BC844": [1610, "(1 to 4 %) to > 65 % cover"],
        "#9AC79C": [1612, "(1 to 4 %) to (40 to 65 %) cover"],
        "#B4C769": [1613, "(1 to 4 %) to (15 to 40 %) cover"],
        "#C88A60": [1615, "(1 to 4 %) to (4 to 15 %) cover"],
        "#9AC79C": [1616, "Remained as 1 to 4 % cover"],
        "#75B476": [1515, "Remained as 4 to 15 % cover"],
        "#A5DE3C": [1313, "Remained as 15 to 40 % cover"],
        "#2D8D2F": [1212, "Remained as 40 to 65 % cover"],
        "#0E7912": [1010, "Remained as > 65 % cover"],
    }

    legend_labels = [
        "No Data - Not vegetated",
        "Not-Vegetated to 1 to 4 % cover",
        "Not-Vegetated to 4 to 15 % cover",
        "Not-Vegetated to 15 to 40 % cover",
        "Not-Vegetated to 40 to 65 % cover",
        "Not-Vegetated to > 65 % cover",
        "> 65 % to 40 to 65 % cover",
        "> 65 % to 15 to 40 % cover",
        "> 65 % to 4 to 15 % cover",
        "> 65 % to 1 to 4 % cover",
        "40 to 65 % to > 65 % cover",
        "40 to 65 % to 15 to 40 % cover",
        "40 to 65 % to 4 to 15 % cover",
        "40 to 65 % to 1 to 4 % cover",
        "15 to 40 % to > 65 % cover",
        "15 to 40 % to 40 to 65 % cover",
        "15 to 40 % to 4 to 15 % cover",
        "15 to 40 % to 1 to 4 % cover",
        "4 to 15 % to > 65 % cover",
        "4 to 15 % to 65 % cover",
        "4 to 15 % to 15 to 40 % cover",
        "15 to 40 % to 1 to 4 % cover",
        "1 to 4 % to > 65 % cover",
        "1 to 4 % to 65 % cover",
        "1 to 4 % to 15 to 40 % cover",
        "15 to 40 % to 4 to 15 % cover",
        "Remained as 1 to 4 % cover",
        "Remained as 4 to 15 % cover",
        "Remained as 15 to 40 % cover",
        "Remained as 40 to 65 % cover",
        "Remained as > 65 % cover",
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12, frameon=True, ncol=1)

    # Adjust layout and display
#    plt.tight_layout()
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()


import matplotlib.pyplot as plt
import xarray as xr
import geopandas as gpd

def plot_water_persistence_change(data, cmap, norm, figsize=(12, 8), title='Water Persistence Changes'):
    """
    Plots a water persistence change map using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0.0, "No Data /\n No water"],
        "#1B55BA": [11, "Remained as > 9 months"],
        "#70C89C": [13, "> 9 months to tidal"],
        "#BD88C8": [17, "> 9 months to 7 to 9 months"],
        "#C88CC3": [18, "> 9 months to 4-6 months"],
        "#C877A1": [19, "> 9 months to 1-3 months"],
        "#6C7CC8": [31, "Tidal to non-tidal (> 9 months)"],
        "#2D8D2F": [33, "Remained as tidal"],
        "#7D8EC8": [37, "Tidal to non-tidal (7 to 9 months)"],
        "#8DA4C8": [38, "Tidal to non-tidal (4-6 months)"],
        "#A1B6C8": [39, "Tidal to non-tidal (1-3 months)"],
        "#6488C8": [71, "7 to 9 months to > 9 months"],
        "#84C8B9": [73, "7 to 9 months (non-tidal) to tidal"],
        "#3479C9": [77, "7 to 9 months to 7 to 9 months"],
        "#B5B557": [78, "7 to 9 months to 4-6 months"],
        "#C84922": [79, "7 to 9 months to 1-3 months"],
        "#306FC8": [81, "4-6 months to > 9 months"],
        "#2097C8": [83, "4-6 months (non-tidal) to tidal"],
        "#1087C8": [87, "4-6 months to 7-9 months"],
        "#4F9DD9": [88, "4-6 months to 4-6 months"],
        "#C86032": [89, "4-6 months to 1-3 months"],
        "#1306C8": [91, "1-3 months to > 9 months"],
        "#A0C2C8": [93, "1-3 months (non-tidal) to tidal"],
        "#3420C8": [97, "1-3 months to 7-9 months"],
        "#4E95C8": [98, "1-3 months to 4-6 months"],
        "#71CAFD": [99, "Remained as 1 to 3 months"]
    }

    legend_labels = [
        "No Data /\n No water",
        "Remained as > 9 months",
        "> 9 months to tidal",
        "> 9 months to 7 to 9 months",
        "> 9 months to 4-6 months",
        "> 9 months to 1-3 months",
        "Tidal to non-tidal (> 9 months)",
        "Remained as tidal",
        "Tidal to non-tidal (7 to 9 months)",
        "Tidal to non-tidal (4-6 months)",
        "Tidal to non-tidal (1-3 months)",
        "7 to 9 months to > 9 months",
        "7 to 9 months (non-tidal) to tidal",
        "7 to 9 months to 7 to 9 months",
        "7 to 9 months to 4-6 months",
        "7 to 9 months to 1-3 months",
        "4-6 months to > 9 months",
        "4-6 months (non-tidal) to tidal",
        "4-6 months to 7-9 months",
        "4-6 months to 4-6 months",
        "4-6 months to 1-3 months",
        "1-3 months to > 9 months",
        "1-3 months (non-tidal) to tidal",
        "1-3 months to 7-9 months",
        "1-3 months to 4-6 months",
        "Remained as 1 to 3 months"
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()


def plot_impact(data, cmap, norm, figsize=(12, 8), title='Change impacts'):
    """
    Plots impact changes using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No change"],
        "#CD853F": [1, "Accretion: 1)"],
        "#00FF00": [2, "Algal bloom: 2)"],
        "#D2691E": [3, "Algal dieback: 3)"],
        "#773F1A": [4, "Bare soil exposure: 4)"],
        "#3D0734": [5, "Blackwater event: 5)"],
        "#FFE4B5": [6, "Browning (vegetation): 6)"],
        "#9370DB": [7, "Building or infrastructure abandonment: 7)"],
        "#D0A520": [8, "Compaction: 8)"],
        "#FAFAD2": [9, "Coral bleaching: 9)"],
        "#C71585": [10, "Coral damage: 10)"],
        "#F88379": [11, "Coral recovery: 11)"],
        "#FFB61E": [12, "Crop change in cultivated lands: 12)"],
        "#B87333": [13, "Crop damage: 13)"],
        "#A7FC00": [14, "Crop establishment: 14)"],
        "#FFF000": [15, "Cropland gain: 15)"],
        "#7B3F00": [16, "Cropland loss: 16)"],
        "#CDA976": [17, "Deglaciation: 17)"],
        "#F2F0E6": [18, "Desalinisation: 18)"],
        "#FFAE42": [19, "Desertification: 19)"],
        "#9F8170": [20, "Elevation change: 20)"],
        "#960018": [21, "Erosion: 21)"],
        "#6F00FF": [22, "Flooding: 22)"],
        "#8D2B0B": [23, "Geomorphological change: 23)"],
        "#B0E0E6": [24, "Glaciation: 24)"],
        "#9ACD32": [25, "Greening: 25)"],
        "#B8860B": [26, "Increased sediment load: 26)"],
        "#1E90FF": [27, "Inundation: 27)"],
        "#CF1020": [28, "Lava flow: 28)"],
        "#C56210": [29, "Leaf scorch: 29)"],
        "#B3446C": [30, "Mine abandonment: 30)"],
        "#C4AEAD": [31, "Mine expansion: 31)"],
        "#FFDABC": [32, "Natural surface gain: 32)"],
        "#663399": [33, "Natural surface loss: 33)"],
        "#FFFAFA": [34, "Net snow gain (amount): 34)"],
        "#B6AA99": [35, "Net snow loss (amount): 35)"],
        "#C0C0C0": [36, "Net snow gain (extent): 36)"],        
        "#EE1C1C": [37, "Net snow loss (extent): 37)"],
        "#FFFAF0": [38, "Net snow gain (hydroperiod): 38)"],
        "#DCDCDC": [39, "Net snow loss (hydroperiod): 39)"],
        "#DAA520": [40, "Phenological change: 40)"],
        "#4B0082": [41, "Railway or road abandonment: 41)"],
        "#F08080": [42, "Railway or road construction: 42)"],
        "#FFA500": [43, "Receding Flood: 43)"],
        "#EE82EE": [44, "Salinisation: 44)"],
        "#B0C4DE": [45, "Sea ice decrease: 45)"],
        "#D7F6F5": [46, "Sea ice increase: 46)"],
        "#008B8B": [47, "Sea level fall: 47)"],
        "#00BFFF": [48, "Sea level rise: 48)"],
        "#E9967A": [49, "Sedimentation: 49)"],
        "#F0FFF0": [50, "Sink hole: 50)"],
        "#F0F8FF": [51, "Snow accumulation: 51)"],
        "#A9A9A9": [52, "Snow melt: 52"],
        "#C71585": [53, "Urban area loss: 53"],
        "#9F00FF": [54, "Urban damage: 54"],
        "#CC9898": [55, "Urban decay: 55"],
        "#E52B50": [56, "Urban densification: 56"],
        "#FE6F5E": [57, "Urban development: 57"],
        "#E34234": [58, "Urban growth: 58"],
        "#FFB6C1": [59, "Urban renewal: 59"],
        "#CC3333": [60, "Urban sprawl: 60"],
        "#F06000": [61, "Vegetation damage: 61"],
        "#80FF9F": [62, "Vegetation dieback: 62"],
        "#63A950": [63, "Vegetation gain (amount): 63"],
        "#00755E": [64, "Vegetation gain (extent): 64"],
        "#EEE88A": [65, "Vegetation health deterioration: 65"],
        "#00CC99": [66, "Vegetation health improvement: 66"],
        "#FF8C00": [67, "Vegetation loss (extent): 67"],
        "#DC8C00": [68, "Vegetation reduction (amount): 68"],
        "#B28C00": [69, "Vegetation reduction in understorey (amount): 69"],
        "#F5FFFA": [70, "Vegetation species change: 70"],
        "#AFEEEE": [71, "Water depth decrease: 71"],
        "#9400D3": [72, "Water depth increase: 72"],
        "#00FFFF": [73, "Water gain (extent): 73"],
        "#FFB6C1": [74, "Water loss (extent): 74"],
        "#00FFFF": [75, "Water quality change: 75"]
    }

    legend_labels = [
        "No change", 
        "Accretion: 1", 
        "Algal bloom: 2", 
        "Algal dieback: 3", 
        "Bare soil exposure: 4", 
        "Blackwater event: 5", 
        "Browning (vegetation): 6", 
        "Building or infrastructure abandonment: 7", 
        "Compaction: 8", 
        "Coral bleaching: 9", 
        "Coral damage: 10", 
        "Coral recovery: 11", 
        "Crop change in cultivated lands: 12", 
        "Crop damage: 13", 
        "Crop establishment: 14", 
        "Cropland gain: 15", 
        "Cropland loss: 16", 
        "Deglaciation: 17", 
        "Desalinisation: 18", 
        "Desertification: 19", 
        "Elevation change: 20", 
        "Erosion: 21", 
        "Flooding: 22", 
        "Geomorphological change: 23", 
        "Glaciation: 24", 
        "Greening: 25", 
        "Increased sediment load: 26", 
        "Inundation: 27", 
        "Lava flow: 28", 
        "Leaf scorch: 29", 
        "Mine abandonment: 30", 
        "Mine expansion: 31", 
        "Natural surface gain: 32", 
        "Natural surface loss: 33", 
        "Net snow gain (amount): 34", 
        "Net snow loss (amount): 35",  
        "Net snow gain (extent): 36", 
        "Net snow loss (extent): 37", 
        "Net snow gain (hydroperiod): 38", 
        "Net snow loss (hydroperiod): 39", 
        "Phenological change: 40",
        "Railway or road abandonment: 41", 
        "Railway or road construction: 42", 
        "Receding Flood: 43", 
        "Salinisation: 44", 
        "Sea ice decrease: 45", 
        "Sea ice increase: 46", 
        "Sea level fall: 47", 
        "Sea level rise: 48", 
        "Sedimentation: 49", 
        "Sink hole: 50", 
        "Snow accumulation: 51", 
        "Snow melt: 52", 
        "Urban area loss: 53", 
        "Urban damage: 54", 
        "Urban decay: 55", 
        "Urban densification: 56", 
        "Urban development: 57", 
        "Urban growth: 58", 
        "Urban renewal: 59", 
        "Urban sprawl: 60", 
        "Vegetation damage: 61",
        "Vegetation dieback: 62",
        "Vegetation gain (amount): 63",
        "Vegetation gain (extent): 64",
        "Vegetation health deterioration: 65",
        "Vegetation health improvement: 66",
        "Vegetation loss (extent): 67",
        "Vegetation reduction (amount): 68",
        "Vegetation reduction in understorey (amount): 69",
        "Vegetation species change: 70",
        "Water depth decrease: 71",
        "Water depth increase: 72",
        "Water gain (extent): 73",
        "Water loss (extent): 74",
        "Water quality change: 75"
    ]

def plot_impact_mychanges(data, cmap, norm, figsize=(12, 8), title='Change impacts'):
    """
    Plots impact changes using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No change"],
        #"#6F00FF": [22, "Flooding: 22"],
        #"#1E90FF": [27, "Inundation: 27"],
        #"#FFFAF0": [38, "Net snow gain (hydroperiod): 38)"],
        #"#DCDCDC": [39, "Net snow loss (hydroperiod): 39)"],
        #"#F06000": [61, "Vegetation damage: 61"],
        #"#FFD580": [62, "Vegetation dieback: 62"],
        "#63A950": [63, "Vegetation gain (amount): 63"],
        "#00755E": [64, "Vegetation gain (extent): 64"],
        "#DC8C00": [67, "Vegetation loss (extent): 67"],
        "#FF8C00": [68, "Vegetation reduction (amount): 68"], 
        #"#AFEEEE": [71, "Water depth decrease: 71"],
        #"#9400D3": [72, "Water depth increase: 72"],
        #"#00FFFF": [73, "Water gain (extent): 73"],
        #"#FFB6C1": [74, "Water loss (extent): 74"],
        #"#00FFFF": [75, "Water quality change: 75"]
    }

    legend_labels = [
        "No change",
        #"Flooding: 22",
        #"Inundation: 27",
        #"Net snow gain (hydroperiod): 38)",
        #"Net snow loss (hydroperiod): 39)",    
        #"Vegetation damage: 61",
        #"Vegetation dieback: 62",
        "Vegetation gain (amount): 63",
        "Vegetation gain (extent): 64",
        "Vegetation loss (extent): 67",
        "Vegetation reduction (amount): 68",
        #"Water depth decrease: 71",
        #"Water depth increase: 72",
        #"Water gain (extent): 73",
        #"Water loss (extent): 74",
        #"Water quality change: 75",
    ]
    
    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

def plot_impact_mychanges_loss(data, cmap, norm, figsize=(12, 8), title='Change impacts'):
    """
    Plots impact changes using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No change"],
        #"#6F00FF": [22, "Flooding: 22"],
        #"#1E90FF": [27, "Inundation: 27"],
        #"#FFFAF0": [38, "Net snow gain (hydroperiod): 38)"],
        #"#DCDCDC": [39, "Net snow loss (hydroperiod): 39)"],
        #"#F06000": [61, "Vegetation damage: 61"],
        #"#80FF9F": [62, "Vegetation dieback: 62"],
        "#63A950": [63, "Vegetation gain (amount): 63"],
        #"#6A5ACD": [64, "Vegetation gain (extent): 64"],##00755E
        "#FF8C00": [68, "Vegetation reduction (amount): 68"], ##FF8C00
        #"#DC8C00": [67, "Vegetation loss (extent): 67"],
        #"#AFEEEE": [71, "Water depth decrease: 71"],
        #"#9400D3": [72, "Water depth increase: 72"],
        #"#00FFFF": [73, "Water gain (extent): 73"],
        #"#FFB6C1": [74, "Water loss (extent): 74"],
        #"#00FFFF": [75, "Water quality change: 75"]
    }

    legend_labels = [
        "No change",
        #"Flooding: 22",
        #"Inundation: 27",
        #"Net snow gain (hydroperiod): 38)",
        #"Net snow loss (hydroperiod): 39)",    
        #"Vegetation damage: 61",
        #"Vegetation dieback: 62",
        "Vegetation gain (amount): 63",
        #"Vegetation gain (extent): 64",
        "Vegetation reduction (amount): 68",
        #"Vegetation loss (extent): 67",
        #"Water depth decrease: 71",
        #"Water depth increase: 72",
        #"Water gain (extent): 73",
        #"Water loss (extent): 74",
        #"Water quality change: 75",
    ]
    
    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

def plot_impact_mychanges_damage(data, cmap, norm, figsize=(12, 8), title='Change impacts'):
    """
    Plots impact changes using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "No change"],
        #"#6F00FF": [22, "Flooding: 22"],
        #"#1E90FF": [27, "Inundation: 27"],
        #"#FFFAF0": [38, "Net snow gain (hydroperiod): 38)"],
        #"#DCDCDC": [39, "Net snow loss (hydroperiod): 39)"],
        "#F06000": [61, "Vegetation damage: 61"],
        #"#80FF9F": [62, "Vegetation dieback: 62"],
        #"#63A950": [63, "Vegetation gain (amount): 63"],
        #"#6A5ACD": [64, "Vegetation gain (extent): 64"],##00755E
        #"#FF8C00": [68, "Vegetation reduction (amount): 68"], ##FF8C00
        #"#DC8C00": [67, "Vegetation loss (extent): 67"],
        #"#AFEEEE": [71, "Water depth decrease: 71"],
        #"#9400D3": [72, "Water depth increase: 72"],
        #"#00FFFF": [73, "Water gain (extent): 73"],
        #"#FFB6C1": [74, "Water loss (extent): 74"],
        #"#00FFFF": [75, "Water quality change: 75"]
    }

    legend_labels = [
        "No change",
        #"Flooding: 22",
        #"Inundation: 27",
        #"Net snow gain (hydroperiod): 38)",
        #"Net snow loss (hydroperiod): 39)",    
        "Vegetation damage: 61",
        #"Vegetation dieback: 62",
        #"Vegetation gain (amount): 63",
        #"Vegetation gain (extent): 64",
        #"Vegetation reduction (amount): 68",
        #"Vegetation loss (extent): 67",
        #"Water depth decrease: 71",
        #"Water depth increase: 72",
        #"Water gain (extent): 73",
        #"Water loss (extent): 74",
        #"Water quality change: 75",
    ]
    
    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

####  PLOTTING FUNCTIONS

def stat_summary(xarr, scheme):
    # Search habitat types in farm 
    lc_types = np.unique(xarr, return_counts=True)
    
    # Create dictionary of habitats with respective area in hectares
    landcover_stat_dict = {}
    for color, label in scheme.items():
        if((label[0] in lc_types[0]) & (label[0]!=0)):
            landcover_stat_dict[label[1]] = lc_types[1][list(lc_types[0]).index(label[0])]*100/10000 

    # Add total area
    landcover_stat_total_dict = {"TOTAL": round(sum(landcover_stat_dict.values())*625,2)}

    # Calculate percentage of each habitat
    for label, value in landcover_stat_dict.items():
        percentage = round(value/landcover_stat_total_dict["TOTAL"]*100, 2)
        landcover_stat_dict[label] = [value, percentage]

    ## Python program to print the habitat details into table 
    print ("{:<54} {:<10} {:<20}".format("\033[1m" +'CATEGORY','HECTARE', "PERCENT"+"\033[0m"))
    for k, v in landcover_stat_dict.items():
        hect, perc = v
        print ("{:<50} {:<10} {:<20}".format(k, hect, perc))
    ## Python program to print TOTAL into table
    for k, v in landcover_stat_total_dict.items():
        print ("{:<50} {:<10}".format(k, v))

####  CHANGE FUNCTIONS
def create_impact_mask(obs_change_l3, obs_change_vcov, l3_value=124124, vcov_values=[1012, 1013, 1015, 1016, 1213, 1215, 1216]):
    """
    Creates a mask with 1s for specified 'impact' conditions and 0s elsewhere.
    
    Parameters:
        obs_change_l3 (array): Array with l3 classification values.
        obs_change_vcov (array): Array with vcov classification values.
        l3_value (int): The specific value in obs_change_l3 to match (default is 124124).
        vcov_values (list of int): List of vcov values to match in obs_change_vcov (default includes 1012, 1013, 1015, 1016, 1213, 1215, 1216).
    
    Returns:
        np.array: A mask array with 1s where conditions are met, otherwise 0s.
    """
    # Construct the mask using numpy where condition
    mask = np.where(
        (obs_change_l3 == l3_value) & np.isin(obs_change_vcov, vcov_values),
        1,
        0
    )
    return mask

def vegetation_dieback(data, cmap, norm, figsize=(12, 8), title='Vegetation dieback'):
    """
    Plots lifeform changes using xarray data and a custom legend.

    Parameters:
    - data (xarray.DataArray): The xarray data to be plotted.
    - cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    - norm (matplotlib.colors.Normalize): Normalization for the colormap.
    - figsize (tuple): The size of the plot figure.
    - title (str): The title of the plot.

    Returns:
    - None: Displays the plot.
    """
    
    # Create the plot figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    
    # Plot the data without the colorbar
    data.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)
    
    # Customize plot aesthetics
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    ax.set_title(title, fontsize=16)
    
    # Define the custom legend colors and labels
    legend_colors = {
        "#FFFFFF": [0, "Background"],
        "#C80000": [1, "Vegetation dieback"]
    }

    legend_labels = [
        "Remained non-vegetated",
        "Vegetation dieback"
    ]

    # Create custom legend handles
    handles = [
        plt.Line2D(
            [0], [0],
            marker='o',
            color='w',
            label=label,
            markerfacecolor=color,
            markersize=10,
            markeredgewidth=0.8,
            markeredgecolor='black'
        ) for label, color in zip(legend_labels, legend_colors)
    ]

    # Add the legend to the plot
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

#  CALCULATE GAINS
def calculate_gains(lc, start_index=0, end_index=-1, ignore_no_change=True):
    """
    Calculate land cover change values between two dates within a time-indexed xarray DataArray,
    create a new DataArray with these values, and convert it into an xarray.Dataset.

    Parameters:
    - lc (xarray.DataArray): The input DataArray with a time dimension for land cover levels.
    - start_index (int): The index of the starting time slice.
    - end_index (int): The index of the ending time slice.
    - ignore_no_change (bool): If True, sets cells with no change to zero.

    Returns:
    - xarray.Dataset: A new Dataset named 'l3_2010_2020' representing changes in land cover.
    """
    # Ensure indices are within bounds
    if start_index >= lc.time.size or end_index >= lc.time.size:
        raise IndexError("start_index or end_index is out of bounds for the time dimension.")

    # Select start and end dates for comparison, converting to int32 to allow for larger values
    start = lc.isel(time=start_index).astype(np.int32)
    end = lc.isel(time=end_index).astype(np.int32)

    # Calculate change values, combining start and end into a single array
    change_vals = (start * 1000) + end
    if ignore_no_change:
        change_vals = np.where(start == end, 0, change_vals)

    # Retrieve spatial coordinates and attributes from the initial level
    level_3 = lc.isel(time=start_index).drop_vars("time")

    # Create a new DataArray for observed changes
    obs_gain_l3_2010_2020 = xr.DataArray(
        data=change_vals,
        coords=level_3.coords,
        dims=level_3.dims,
        name="observed change",
        attrs=level_3.attrs,
        fastpath=False,
    )

    # Convert DataArray to a Dataset
    obs_gain_l3 = obs_gain_l3_2010_2020.to_dataset(name="l3_2010_2020")

    # Clean up by deleting the original DataArray (optional if not needed)
    del obs_gain_l3_2010_2020

    return obs_gain_l3

# Example usage
# obs_gain_l3 = calculate_change_dataset(lc.level3, start_index=0, end_index=-1, ignore_no_change=True)


##  CALCULATE LOSSES
def calculate_losses(lc, start_index=0, end_index=-1, ignore_no_change=True):
    """
    Calculate land cover change values between two dates within a time-indexed xarray DataArray,
    create a new DataArray with these values, and convert it into an xarray.Dataset.

    Parameters:
    - lc (xarray.DataArray): The input DataArray with a time dimension for land cover levels.
    - start_index (int): The index of the starting time slice.
    - end_index (int): The index of the ending time slice.
    - ignore_no_change (bool): If True, sets cells with no change to zero.

    Returns:
    - xarray.Dataset: A new Dataset named 'l3_2010_2020' representing changes in land cover.
    """
    # Ensure indices are within bounds
    if start_index >= lc.time.size or end_index >= lc.time.size:
        raise IndexError("start_index or end_index is out of bounds for the time dimension.")

    # Select start and end dates for comparison, converting to int32 to allow for larger values
    start = lc.isel(time=start_index).astype(np.int32)
    end = lc.isel(time=end_index).astype(np.int32)

    # Calculate change values, combining start and end into a single array
    change_vals = (end * 1000) + start
    if ignore_no_change:
        change_vals = np.where(start == end, 0, change_vals)

    # Retrieve spatial coordinates and attributes from the initial level
    level_3 = lc.isel(time=start_index).drop_vars("time")

    # Create a new DataArray for observed changes
    obs_loss_l3_2010_2020 = xr.DataArray(
        data=change_vals,
        coords=level_3.coords,
        dims=level_3.dims,
        name="observed change",
        attrs=level_3.attrs,
        fastpath=False,
    )

    # Convert DataArray to a Dataset
    obs_loss_l3 = obs_loss_l3_2010_2020.to_dataset(name="l3_2010_2020")

    # Clean up by deleting the original DataArray (optional if not needed)
    del obs_loss_l3_2010_2020

    return obs_loss_l3

# Example usage
# obs_gain_l3 = calculate_change_dataset(lc.level3, start_index=0, end_index=-1, ignore_no_change=True)



### FUNCTIONS FOR PLOTTING
import matplotlib.pyplot as plt
import xarray as xr
from mycolourschemes import l3change_colors as legend_colors, l3change_labels as legend_labels  # Import color scheme

def plot_level3_gains(obs_gain_l3, cmap, norm, title='Level 3 Gains: 2010 to 2020'):
    """
    Plot Level 3 gains from 2010 to 2020.

    Parameters:
    obs_gain_l3 (xarray.DataArray): The xarray data array to plot.
    cmap (matplotlib.colors.Colormap): The colormap to use for the plot.
    norm (matplotlib.colors.Normalize): Normalization to use for the colormap.
    title (str): The title of the plot.
    """

    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot the xarray data without the colorbar
    c = obs_gain_l3.l3_2010_2020.plot(ax=ax, cmap=cmap, norm=norm, add_colorbar=False)

    # Pretty plot options
    ax.margins(0.05)
    ax.set_aspect('equal', adjustable='datalim')
    ax.set_xlabel('Longitude', fontsize=12)  # Set x-axis label
    ax.set_ylabel('Latitude', fontsize=12)  # Set y-axis label
    ax.set_title(title, fontsize=16)

    # Create custom legend handles
    handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, 
                           markerfacecolor=color, markersize=10,
                           markeredgewidth=0.8, markeredgecolor='black') 
               for color, label in zip(legend_colors.keys(), legend_labels)]

    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5), 
              fontsize=10, title='', title_fontsize='13', frameon=True)

    plt.tight_layout()
    plt.show()
