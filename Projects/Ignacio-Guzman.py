planets = ("Mercury", "Venus", "Earth","Mars", "Jupiter","Saturn","Uranus" , "Neptune")
g_ms2   = [3.7, 8.87 ,9.81, 3.711, 24.79, 10.44 , 8.69, 11.5]

print("Calculate your weight in a diffrent planet")

myWeigh = int(input("What is your weight (pounds)?")
myplanet = input(f"Select a planet from the list:  {Planets}")

def calculateWeight(planet, mass ) :
        print(f"/nEarth mass in pounds is : {mass})

w_kg= mass / 2.2046
 print(f"Mass in kg : {w_kg}")

n_lb = 4.45 

planet_index = planet.index(planet)
print(f"Weight in {planets[planet_index]}mmis {w_kg * g_ms[planet_index])  / n_lb} lb")


calculateWeight(myPlanet , myWeigh)

