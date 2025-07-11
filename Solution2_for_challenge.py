import numpy as np

#Solution2
dailywts = 185 - np.arange (5*7)/5
weeklywts = dailywts.reshape(5,7)
print('Your weight in your fast',dailywts)

days = {
    'Monday' : weeklywts[:,0],
    'Tuesday' : weeklywts[:,1],
    'Wednesday' : weeklywts[:,2],
    'Thursday' : weeklywts[:,3],
    'Friday ' : weeklywts[:,4],
    'Saturday' : weeklywts[:,5],
    'Sunday' : weeklywts[:,6]
}

for days, value in days.items():
   print(f'Your weight in these days :,{days} : ,{value}')
