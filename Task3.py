import pandas as pd


#§ Read the dataset.
data = pd.read_csv("c:/Users/Gumede/Downloads/motor_insure.csv (1)/motor_data11-14lats.csv")


#§ Inspects its column by displaying the first 10 records.
print(data.head(10))



#§ Display records for 'make' and 'usage' for 'sets_num' that are more than 40.

#print(data[data['sets_num']> 40] ['make','usage'])


#§ Plot a basic graph showing effective_yr on y axes and carrying capacity on x-axes

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.ylabel('EFFECTIVE YEAR')
plt.xlabel('CARRYING CAPACITY')
plt.title('Effective Year VS Car Capacity')
plt.show()