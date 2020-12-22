#Measure ejection fraction
#
#The ejection fraction is defined as:
#
#(Vmax-Vmin)/Vmax
#
#...where V is left ventricle volume for one 3D timepoint.

#To close our investigation, plot slices from the maximum and minimum volumes by analyzing the volume time series (ts). Then, calculate the ejection fraction.
#After calculating the ejection fraction, review the chart below. Should this patient be concerned?

#Ch3_L1_EjFracPath.png

# Get index of max and min volumes
tmax = np.argmax(ts)
tmin = np.argmin(ts)

# Plot the largest and smallest volumes
fig, axes = plt.subplots(2,1)
axes[0].imshow(vol_ts[tmax, 4], vmax=160)
axes[1].imshow(vol_ts[tmin, 4], vmax=160)
format_and_render_plots()


# Calculate ejection fraction
ej_vol = (ts.max() - ts.min()) 
ej_frac = (ts.max() - ts.min()) / ts.max()
print('Est. ejection volume (mm^3):', ej_vol)
print('Est. ejection fraction:', ej_frac)

#Est. ejection volume (mm^3): 31268.00536236538
#Est. ejection fraction: 0.3202054794520548

#Yes, the ejection fraction is lower than normal.

#Fantastic! This patient has heart failure with infarction - a serious condition. This case study illustrates a typical image analysis workflow: a single, useful metric is the result of a lot of sophisticated preprocessing, segmentation and measurement techniques.
