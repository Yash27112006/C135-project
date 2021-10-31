import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("filtered_data.csv")

star_name = df["Star_name"].to_list()
distance = df["Distance"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
gravity = df["Gravity"].to_list()

print(df.head())

plt.figure(figsize=(10,5))
plt.title("Star name vs Mass")
plt.bar(star_name[0:9],mass[0:9])
plt.show()

plt.figure(figsize=(10,5))
plt.title("Star name vs Radius")
plt.bar(star_name[0:9],radius[0:9])
plt.show()

plt.figure(figsize=(10,5))
plt.title("Star name vs Distance")
plt.bar(star_name[0:9],distance[0:9])
plt.show()

plt.figure(figsize=(10,5))
plt.title("Star name vs Gravity")
plt.bar(star_name[0:9],gravity[0:9])
plt.show()