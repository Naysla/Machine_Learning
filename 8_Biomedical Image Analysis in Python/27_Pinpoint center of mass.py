#Pinpoint center of mass
#The distance transformation reveals the most embedded portions of an object. On the other hand, ndi.center_of_mass() returns the coordinates for the center of an object.
#
#The "mass" corresponds to intensity values, with higher values pulling the center closer to it.
#
#For this exercise, calculate the center of mass for the two labeled areas. Then, plot them on top of the image.

# Extract centers of mass for objects 1 and 2
coms = ndi.center_of_mass(vol, labels,index=[1, 2])
print('Label 1 center:', coms[0])
print('Label 2 center:', coms[1])

# Add marks to plot
for c0, c1, c2 in coms:
    plt.scatter(c2, c1, s=100, marker='o')
plt.show()

#Answer

#Label 1 center: (4.9149927898701, 125.72786150646698, 141.42957762070142)
# Label 2 center: (5.458351990999034, 121.50943176720855, 121.72954667630684)


#Some shapes, such as those with holes, may have a center of mass that is outside of them.