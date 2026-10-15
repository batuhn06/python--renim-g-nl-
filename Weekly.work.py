#1

#From the time when I was just learning about functions.

def greeting(name, age, favorite_food):
    print("Welcome,", name)
    print("Your age is", age)
    print("Your favorite food is", favorite_food)

greeting("batu", "twenty", "türkish mantı")
greeting("mill", "nineteen", "sushi")
greeting("arthur", "thirty three", "hamburger")


#2

#I'm trying to create an application that will add the areas of two different triangles and print the sum to the screen.

def area_triangle(base, height):
	return (base * height)/2	
area_c = area_triangle(15, 17)
area_d = area_triangle(40, 41)
sum = area_c + area_d
print(" The sum of both area is:  "  + str(sum))


#3


#We are trying to define a function that will convert the given hours, minutes, and seconds and display the total seconds on the screen.
def total_second(hour, minutes, second):
    toplam = hour * 3600 + minutes * 60 + second
    return(toplam)

A = total_second(15, 36, 23)
print("Total second is: " + str(A))


#4

print(4<5)
#True
print(1 =="1")
#False
print("Yellow"  >  "Cyan" and  "Brown" > "Magenta")
#False
print(not 45 == "Answer")
#True;
print(8 != 9)
#True
print(25 > 50 or 47*5 < 36*7)
#True


#5

#I'm trying to find out the conditions.

def hint_username(username):
	if len(username) < 3:
		print("İnvalid username. Must be at least 3 characters long.")
		
		
#6

#I will try to build a system that uses if,elif, and else based on the temperature of the water.
#If the water is at 80 degrees or above, filter coffee can be brewed.

def the_temperature_of_the_water(temperature):
    if  temperature >= 80:
    	print("the water temperature is ready for making a filter coffee.")
		
#but if it’s not at 80 degrees, it needs to be heated again.
    else:
    	print("heating the water again.")
    	
#Let's try it.

the_temperature_of_the_water(85)
the_temperature_of_the_water(70)	

#7

#I am trying to build a system that guides individuals through the process of obtaining a driver's license.

def check_exam(point, result):    
    if point < 0 or point > 100:
        print("You have entered an invalid score; please enter it correctly.")        
    elif point >= 70 and result == "positive":
        print("Congratulations dude. You passed everything, take the driver license.")        
    elif point >= 70 and result == "negative":
        print("You passed the theoretical exam but you didn't pass the driving exam so try again.")        
    elif point < 70:
        print("You didn't pass the first exam, try again later.")

#Let's try it.
check_exam(85, "positive")
check_exam(65, "negative")
check_exam(120, "positive")

#8

#This is actually my homework.
#I’ve been hired as a lead software engineer at a space agency. It turns out I’m tasked with writing the launch control algorithm for a rocket headed to Mars.


def rocket_kontrol(weather, fuel_level, astronauts):
	if fuel_level  < 0 or fuel_level > 100:
		print("Fuel gauge faulty, invalid value.")		
#I have added a preliminary protocol for the fuel level.
	elif weather == "stormy":
		print("The weather is not safe for the flighting.")		
#I also added a protocol for the weather.
	elif fuel_level >=85 and astronauts == "ready":
		print("All systems confirmed. Initiating ignition!")		
	elif fuel_level >=85 and astronauts == "unready":
		print("ON HOLD: Fuel is sufficient, but the astronauts are yet to board the spacecraft.")	
	elif fuel_level < 85:
		print("CANCELED: Fuel level insufficient for the Mars mission.")	
	else:
		print("SYSTEM CRASHED: Aliens have infiltrated the code! Or maybe you just pressed the wrong keys. Hit the red button and run!")

#Let's check it.
rocket_kontrol("clear", 95, "ready")
rocket_kontrol("clear", 90, "unready")
rocket_kontrol("stormy", 100, "ready")
rocket_kontrol("clear", 70, "ready")
rocket_kontrol("clear", 150, "ready")
rocket_kontrol("snowy", 85, "alien")
		

						
																		
#Thank you for taking the time to review it.