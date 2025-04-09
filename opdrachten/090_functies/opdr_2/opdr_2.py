def kilometers_naar_miles(kilometers):

    miles = kilometers / 1.609344
    return miles

def miles_naar_kilometers(miles):
    
    kilometers = miles * 1.609344
    return kilometers

kilometers = 1223
miles = 867

omgezette_miles = kilometers_naar_miles(kilometers)
omgezette_kilometers = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {omgezette_miles} miles")
print(f"{miles} miles = {omgezette_kilometers} kilometers")