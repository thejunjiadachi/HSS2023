# HSS2023
Repository used for "II International Conference on Humanities and Social Sciences: Fostering Global Resilience through Cross-cultural Collaboration" in Porto. 


## Overview

* Recorded make-up steps of make-up tutorial videos that match the following themes in a csv file:
Natural, Gal, Autumn, Quirky, Korean, Private, Public
* Applied network analsis to 5 make-up genres and 2 scene make-up steps.


## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)
- [Output](#output)
- [Visualization](#visualization)
- [Links](#links)


## Requirements

* pandas
* networkx
* matplotlib

## Usage
1. Check if Location1 starts on column H and the next one is recorded every other one.
2. Replace the dataset path in the script with your own CSV file path:
```
df = pd.read_csv("path/to/your/dataset.csv", encoding='UTF-8')
```

4. Run the script:
```
python network_analysis_script.py
```
5. The script will analyze each video's network, calculate centrality measures, and display.


## Output
The script provides information on degree centrality, closeness centrality, betweenness centrality, and Page Rank for each video. The results are printed to the console, and network visualizations are displayed.


## Visualization
The script generates network visualizations using Matplotlib. Each visualization represents the network structure of a video.

## Links
[HSS2023](https://hss23.sciencesconf.org/)
