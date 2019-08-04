# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head()
#Code starts here



# --------------
#Code starts here
#data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')





data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))
#print(data[data['Total_Summer']==data['Total_Winter']])
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)
print(type(data['Better_Event']))




# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)
print(top_countries.tail(3))
#col='Total_Summer'
#print(list(top_countries.nlargest(10,col)['Country_Name']))
def top_ten(top_countries,col):
    country_list=list(top_countries.nlargest(10,col)['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
a=set(top_10_summer)
b=set(top_10_winter)
c=a.intersection(b)
d=set(top_10)
e=c.intersection(d)
common=list(e)
print(common)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
ax_1=plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax_2=plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
ax_3=plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
#plt.xlabel('Country Name')
#plt.ylabel('Total Medal Count')
plt.title('Summer')
plt.title('Winter')
plt.title('Total')
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']
print(summer_max_ratio)
print(summer_country_gold)
print(winter_max_ratio)
print(winter_country_gold)
print(top_max_ratio)
print(top_country_gold)


# --------------
#Code starts here
data_1=data.drop(data.tail(1).index)
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']
print(most_points)
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True, figsize=(15,10))
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


