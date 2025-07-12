#You decide to invest in a series of billboards along interstate 10 to advertise your stylish new chicken restaurant, Chic-fil-A. You buy three billboards evenly spaced starting on mile marker 17 and ending on mile marker 28. Then you buy another three billboards evenly spaced starting on mile marker 32 and ending on mile marker 36. In order, from mile marker 17 to 36, your billboards display these ads: A, B, C, C, B, A.
#Determine how far each "C" ad is from your restaurant which is located at mile marker 30.

def calculate_billboard_distances():
    # Define billboard sets with start, end, number of billboards, and ad sequence
    billboard_sets = [
        {"start": 17, "end": 28, "count": 3, "ads": ["A", "B", "C"]},
        {"start": 32, "end": 36, "count": 3, "ads": ["C", "B", "A"]}
    ]
    
    restaurant_location = 30
    c_locations = []
    
    for set_info in billboard_sets:
        start = set_info["start"]
        end = set_info["end"]
        count = set_info["count"]
        ads = set_info["ads"]
        
        # Calculate spacing between billboards
        spacing = (end - start) / (count - 1)
        
        # Generate mile markers for this set
        mile_markers = [start + i * spacing for i in range(count)]
        
        # Pair mile markers with ads and collect "C" locations
        for marker, ad in zip(mile_markers, ads):
            if ad == "C":
                c_locations.append(marker)
    
    # Calculate distances from restaurant
    distances = [abs(loc - restaurant_location) for loc in c_locations]
    
    return distances

# Calculate and print the distances
distances = calculate_billboard_distances()
print(f"Each 'C' ad is {distances[0]} miles from the restaurant at mile marker 30.")