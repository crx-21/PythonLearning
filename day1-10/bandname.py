print("Welcome to the Band Name Generator!")
print("What's the name of the city you grew up in?")
city = input()
print("What's the name of a pet?")
pet = input()
numefull = city + pet
print("Your band name could be " + city + " " + pet)
print("Length-ul la tot numele este: " + str(len(numefull)))

optional = city
city = pet
pet = optional  

print("Your band name switched up could be " + city + " " + pet)