import numpy as np

#Solution1
dailywts = 185 - np.arange (5*7)/5
print(dailywts)

Monday = dailywts[0::6]
Tuesday = dailywts[1::6]
Wednesday = dailywts[2::6]
Thurday = dailywts[3::6]
Friday = dailywts[4::6]
Saturday = dailywts[5::6]
Sunday = dailywts[6::6]

print(Monday)
print(Tuesday)
print(Wednesday)
print(Thurday)
print(Friday)
print(Saturday)
print(Sunday)