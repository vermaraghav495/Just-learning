#You’re planning rest stops along a straight highway for a marathon. 
# The course starts at mile marker 5 and ends at mile marker 26.
# You want to place 4 rest stops evenly spaced between these markers. 
# Each rest stop has a supply type in this order:
print('Hello World')
def Stops():
    #define the stops that we named in their sequence
    MarathonStops = [
        {'Start' : 5 , 'End' : 26 ,'Count' : 4, 'Stops' : ['Stop 1','Stop 2','Stop 3','Stop 4']},
         ]
   

    for info in MarathonStops:
        Start = info['Start']  
        End = info['End']
        Stops = info['Stops']
        Count = info['Count']

        spacing = (End - Start ) / (Count-1)
        print(spacing,'is the the spacing between stops')
        
        for i in range(Count):
            position = Start + i * spacing
            print(position,"is the mile marker for", Stops[i])
Stops()