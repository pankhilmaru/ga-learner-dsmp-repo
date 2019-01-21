# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=',',skip_header=1)
print(data)
print("-"*50)
census = np.concatenate((data,np.array(new_record)),axis=0)
print(census)






# --------------
#Code starts here
import numpy as np
data = np.genfromtxt(path, delimiter=',',skip_header=1)
print(data)
census = np.concatenate((data,np.array(new_record)),axis=0)
print(census)
age = np.array(list(census[:,0]))
print(age)
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

print(max_age,min_age)
print(age_mean,age_std)


# --------------
#Code starts here
import numpy as np

race = census[:,2]

race_0 = census[np.where(race == 0)]
race_1 = census[np.where(race == 1)]
race_2 = census[np.where(race == 2)]
race_3 = census[np.where(race == 3)]
race_4 = census[np.where(race == 4)]

print(race_0)
print(race_1)
print(race_2)
print(race_3)
print(race_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

list1 = list([len_0,len_1,len_2,len_3,len_4])
print(list1)

       
value = np.array(list1).min()
#print(value)

minority_race = list1.index(value)
print(minority_race)






# --------------
#Code starts here

import numpy as np
senior_citizens = census[census[:,0]>60]


working_hours_sum = np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len


print(avg_working_hours)



# --------------
#Code starts here

high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high)
print(avg_pay_low)




