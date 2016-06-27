import selenuim
import time


def main():
	driver = webdriver.Firefox()
	driver.get("http://www.listentoyoutube.com/")
	link = "https://www.youtube.com/watch?v=NjOiKLTdUHA"
	textbox = driver.find_element_by_name("url")
	textbox.send_keys(link)
	submit_button = driver.find_element_by_name("submit")
	submit_button.click()
	link_element = wait_for_link(driver)
	link_element.click()

def wait_for_link(driver):
	while True:
		link_element = get_link_element(driver)
		if link_element:
			return link_element
		time.sleep(1)

def get_link_element(driver):
	links_element = driver.find_elements_by_tag_name("a")
	for element in links_element:
		if element.text == "CLICK HERE to get your Download Link":
			return element
	return None


main()