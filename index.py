from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import Nominatim
from haversine import haversine, Unit

if __name__ == '__main__':
    geolocator = Nominatim(user_agent='ISS_Tracker')
    driver = webdriver.Chrome()
    url = driver.get('http://wsn.spaceflight.esa.int/iss/index_portal.php')

    user_city = geolocator.geocode(input("Enter your city "))
    user_location = user_city.latitude, user_city.longitude
    print("Your latitude and longitude is: ", user_location)
    iss_latitude = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[text()='Latitude']//following::div[1]"))).get_attribute("innerHTML")

    iss_latitude_float = (float(iss_latitude.split(" ")[0].replace(",", ".")))

    iss_longitude = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[text()='Longitude']//following::div[1]"))).get_attribute("innerHTML")

    iss_longitude_float = (
        float(iss_longitude.split(" ")[0].replace(",", ".")))

    iss_speed = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[text()='Speed']//following::div[1]"))).get_attribute("innerHTML")
    int_iss_speed = [iss_speed.replace("km/h", "") for speed in iss_speed]

    print("The speed of the ISS is: ", iss_speed, " Latitude: ",
          iss_latitude_float, " Longitude: ", iss_longitude_float)

    iss_location = iss_latitude_float, iss_longitude_float
    distance = haversine(user_location, iss_location, unit=Unit.MILES)
    print("You are", distance, "miles away from the ISS")
    kph_to_mph = (int(int_iss_speed[0]) / 1.609)
    print(kph_to_mph)
    print("The ISS will be over your city in about ", kph_to_mph // distance, " hours")

    driver.close()
