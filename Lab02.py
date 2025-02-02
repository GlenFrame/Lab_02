#!/usr/bin/env python3
import math
name = "Glen Frame"
age = 18
height = 6.333
favorite_color = "Teal"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color) #it does add a space between the variables

print(f"Hello: my name is {name}, my favorite color is {favorite_color}, I am {age} years old, and {height} feet tall!")
height2 = height + 10000 # added 10000 to height to make scientific notation more interesting
print(f"Hello: my name is {name:.4s}, my favorite color is {favorite_color:>5}, I am {age:.4f} years old, and {height2:e} feet tall!")

print(f"""
     Name: {name}
   Age: {age}
      Height: {height}
   Favorite color: {favorite_color}
""")
r = 5
circle_area = math.pi*(r**2)
print(f"the area is {circle_area:.1f}")

sqrt_age = math.sqrt(age)
print(f"The square root of my age is {sqrt_age}")
sin_height = math.sin(height)
cos_height = math.cos(height)
print(f"The sin of height is {sin_height} and the cos of height is {cos_height}")

print(f"""Sum of age and 5: {age + 5}
difference between height and 4: {height - 4}
product of age and height: {age * height}
quotient of height and 2: {height / 2}
remainder of age divided by 3: {age % 3}
age raised to the power of 2: {age**2}""")
temp_fahrenheit = input("Enter a temperature in Fahrenheit")
temp_celsius = (float(temp_fahrenheit) - 32) * 5/9
print(f"{temp_fahrenheit}°Fahrenheit in Celsius is {temp_celsius}°C")