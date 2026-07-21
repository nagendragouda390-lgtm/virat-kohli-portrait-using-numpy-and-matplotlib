import pandas as pd 


df = pd.read_csv('data.csv')

print(df.columns)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.scatter(df['x']/10,df['y']/10,color='black',s=1)
plt.title("Virat's portrait by coding",color="red")
plt.xlabel("X coordinate")
plt.ylabel("y coordinate")

plt.savefig('image.png')
plt.show()
