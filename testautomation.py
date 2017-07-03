from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.eventcinema.co.nz")
#
# first_movie = driver.find_element_by_xpath("html/body/div[5]/div/div[1]/div[4]/div/div[2]/div[2]/div[1]/a[1]/div[2]/span")
# second_movie = driver.find_element_by_xpath("html/body/div[5]/div/div[1]/div[4]/div/div[2]/div[3]/div[1]/a[1]/div[2]/span")
# third_movie = driver.find_element_by_xpath("html/body/div[5]/div/div[1]/div[4]/div/div[2]/div[4]/div[1]/a[1]/div[2]/span")
movie_names=[]
movie_complete=""
for counter in range(2,6):
    print counter
    movie_xpaths= "html/body/div[5]/div/div[1]/div[4]/div/div[2]/div["+str(counter)+"]/div[1]/a[1]/div[2]/span"
    print movie_xpaths
    movie=driver.find_element_by_xpath(movie_xpaths)
    print movie.text
    # movie_names.append(str(movie.text))
    movie_complete += str(movie.text) + " "

# for counter in range(0,3):
#         movie_complete += movie_names(counter)

alexa_phrase= "The new movies that are available in event cinemas are " + movie_complete
print alexa_phrase
# print "The new movies available in event cinemas are " +

# elem = driver.find_element_by_xpath("html/body/div[5]/div/div[1]/div[2]/div[3]")
# elem.clear()
# print elem
# elem=elems.text
# elem = ""
# elem= elem + " " + first_movie.text + " " + second_movie.text + " " + third_movie.text
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# driver.save_screenshot('screenshot.png')
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# print str(elem)
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
