import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pandas.plotting import parallel_coordinates
from pandas.plotting import andrews_curves



matplotlib.style.use("ggplot")

df = pd.read_csv("Dataset\wheat.data", index_col = 0)

df_area_per = df.loc[:,"area": "perimeter"]
df_groove_asym = df.loc[:, "asymmetry" : "groove"]
df_wheat_type = df.loc[:,"compactness": ]

#hist
df_area_per.plot.hist(df_area_per,alpha =0.75)
plt.title("Hist Area&Perimeter")
df_groove_asym.plot.hist(df_groove_asym, alpha =0.75)
plt.title("Hist Asymmetry&Groove")
plt.show()

#scatter plot
plt.scatter(df.area, df.perimeter, c = "Green")
plt.xlabel("Area")
plt.ylabel("Perimeter")
plt.title("Area&Perimeter")
plt.grid(True)
plt.show()

plt.scatter(df.groove, df.asymmetry, c = "blue")
plt.xlabel("Groove")
plt.ylabel("Asymmetry")
plt.title("Asymmetry&Groove")
plt.grid(True)
plt.show()

#3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
ax.scatter(df.area, df.perimeter, df.asymmetry, c='red', marker='.')
plt.title("3D Area&PerimeterAsymmetry")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('width')
ax.set_ylabel('asymmetry')
ax.set_zlabel('groove')
ax.scatter(df.width, df.asymmetry, df.groove, c='green', marker='.')
plt.title("3D Width&Asymmetry&Groove")
plt.show()

#parallel coordinates
plt.figure()
parallel_coordinates(df_wheat_type, "wheat_type",  alpha = 0.4)
plt.title("Wheat type (parallel coordinates)")
plt.show()

#Andrews curve
plt.figure()
andrews_curves(df_wheat_type, "wheat_type")
plt.title("Wheat type (Andrew's curve)")
plt.show()

#boxplot
df.boxplot(column=['area','perimeter'], vert = False)
plt.title("Box plot ")
plt.show()

#plt.imshow()
df.corr()
plt.imshow(df.corr(), cmap=plt.cm.Greens)
plt.colorbar()                                             #colors&name_axis
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)
plt.title("Correlation between features")
plt.show()

