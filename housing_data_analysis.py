import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('californiahouse.csv')
df=pd.DataFrame(data)
df=df.dropna()
df['room_per_person']=df['total_rooms']/df['households']
near_ocean=df[df['ocean_proximity']=='NEAR BAY']
far_ocean=df[df['ocean_proximity']=='INLAND']
near_ocean_cost=near_ocean['median_house_value'].mean()
far_ocean_cost=far_ocean['median_house_value'].mean()
print(near_ocean_cost)
print(far_ocean_cost)
plt.figure(figsize=(10,6))
plt.scatter(x=df['longitude'],y=df['latitude'],alpha=0.4,c=df['median_house_value'],cmap='jet')
plt.colorbar()
plt.title('House values based on ocean')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()

    

