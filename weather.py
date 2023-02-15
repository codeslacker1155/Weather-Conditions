# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json, math

# Enter your API key here
api_key = "b5a8d5ede42353c3cd7b9089cbea7ddb"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# print banner
print("""
__        __         _   _                     ____                _ _ _   _                 
\ \      / /__  __ _| |_| |__   ___ _ __      / ___|___  _ __   __| (_) |_(_) ___  _ __  ___ 
 \ \ /\ / / _ \/ _` | __| '_ \ / _ \ '__|____| |   / _ \| '_ \ / _` | | __| |/ _ \| '_ \/ __|
  \ V  V /  __/ (_| | |_| | | |  __/ | |_____| |__| (_) | | | | (_| | | |_| | (_) | | | \__ \\
   \_/\_/ \___|\__,_|\__|_| |_|\___|_|        \____\___/|_| |_|\__,_|_|\__|_|\___/|_| |_|___/
                                                                                             """)

# Give city, state
city_name = input("Enter city name: ")
state_code= input("Enter state code (ex. South Carolina = SC): ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + ',US-' + state_code 

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

	# store the value of "main"
	# key in variable y
	y = x["main"]

	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]
	celcisus_temp = current_temperature - 273.15
	fahrenheit_temp = celcisus_temp * ( 9 / 5 ) + 32
	fahrenheit_temp = math.floor(fahrenheit_temp)

	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidity = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Estimated average temperature (in fahrenheit) = " +
					str(fahrenheit_temp) +
		"\n Average atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n Average humidity (in percentage) = %" +
					str(current_humidity) +
		"\n Weather Conditions = " +
					str(weather_description))

else:
	print(" Invalid Input. Try Again. ")
