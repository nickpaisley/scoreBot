import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Dev\Resources\chromedriver\chromedriver.exe")  

# Load James Quick's typing game page.
driver.get('https://learnbuildtype.netlify.com/');

# Allow the page to load. 
time.sleep(5) 

# Start the game after the home page loads. 
driver.find_element_by_tag_name('body').send_keys('s') 

# Set your desired score for the typing game
desiredScore = 303

# Once the game has started this loop grabs the randomCharcter to type and enters it. The desiredScore is
# how many times this loop will run. Each loop adds a score of 1. So 303 loops will give a score of 303. 
for i in range(desiredScore):
  rc = (driver.find_element_by_id('randomCharacter')).text
  driver.find_element_by_tag_name('body').send_keys(rc) 

# Give the game time to complete (30 Seconds) and allow the user to input a playerName to save. 
time.sleep(45) 

# Shut the chromeDriver down.
driver.quit()

