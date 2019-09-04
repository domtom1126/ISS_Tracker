import requests
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from geopy.geocoders import Nominatim
from haversine import haversine, Unit

geolocator = Nominatim(user_agent='ISS_Tracker')
driver = webdriver.Safari()
url = driver.get('http://wsn.spaceflight.esa.int/iss/index_portal.php')

user_city = geolocator.geocode(input("Enter your city "))
user_location = user_city.latitude, user_city.longitude
print(user_location)
iss_latitude = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Latitude']//following::div[1]"))).get_attribute("innerHTML")

iss_latitude_float = (float(iss_latitude.split(" ")[0].replace(",",".")))

iss_longitude = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Longitude']//following::div[1]"))).get_attribute("innerHTML")

iss_longitude_float = (float(iss_longitude.split(" ")[0].replace(",",".")))

iss_speed = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Speed']//following::div[1]"))).get_attribute("innerHTML")
print(iss_speed, iss_latitude_float, iss_longitude_float)

iss_location = iss_latitude_float, iss_longitude_float
distance = haversine(user_location, iss_location, unit=Unit.MILES)
print(distance)
driver.close()

