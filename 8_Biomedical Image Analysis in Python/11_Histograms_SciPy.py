#Histograms
#Histograms display the distribution of values in your image by binning each element by its intensity then measuring the size of each bin.
#
#The area under a histogram is called the cumulative distribution function. It measures the frequency with which a given range of pixel intensities occurs.
#
#For this exercise, describe the intensity distribution in im by calculating the histogram and cumulative distribution function and displaying them together.

# Import SciPy's "ndimage" module
import scipy.ndimage as ndi 

# Create a histogram, binned at each possible value
hist = ndi.histogram(im,min=0,max=255,bins=256)

# Create a cumulative distribution function
cdf = hist.cumsum() / hist.sum()

# Plot the histogram and CDF
fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(hist, label='Histogram')
axes[1].plot(cdf, label='CDF')
format_and_render_plot()

#Great work. You can see the data is clumped into a few separate distributions, consisting of background noise, skin, bone, and artifacts. Sometimes we can separate these well with global thresholds (foreground/background); other times the distributions overlap quite a bit (skin/bone).