# experimentsinimagelogs

# Idea

Now that we can read the binary dlis files with the dlisio python package, we are interested in what analysis can be done on image logs' resistivity values.  Can we extract information about the geology and structure by looking at the values themselves instead of just a bitmap image?  Worked on during FORCE Hackathon 2019 in Stavanger, Norway.

![](https://github.com/aruss175/experimentsinimagelogs/blob/master/where%20to%20find%20the%20image%20log.png)

# Purpose

1.  To find keywords in dlis metadata that identify processed image logs
2.  To extract those processed image log channels from dlis
3.  Using the image channels, analyze the histogram of resistivity values at each depth and cluster the histograms.

![](https://github.com/aruss175/experimentsinimagelogs/blob/master/image%20log.PNG)

Warning:  We did discover that sometimes the Static or Dynamic end result channels do not contain resistivity values, but are outputted in color codes!  So, you may have to stitch together each pad channel to create your own final image log channel.

# Data

Data is found [here](https://drive.google.com/open?id=1v_noeFgTZekBzvi6Z3kRneFoBp6D62ru)  This is a small subset of wells with image logs present (both raw and processed) downloaded from the [NOPIMS Australia dataset](https://nopims.dmp.wa.gov.au/Nopims/Search/Wells).

Finding the image logs is a bit of a needle in a haystack - we've written several functions in the functions folder above to help you dig out these files and specific channels!

![](https://github.com/aruss175/experimentsinimagelogs/blob/master/Statistics_Data.PNG)

# Tools
Work done with Python 3.6 and Jupyter Notebooks

# Results

We had the most success with the textural analysis and clustering the resistivity distributions per depth.  Please see the notebooks.
