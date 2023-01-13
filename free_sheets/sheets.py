from cairosvg import svg2pdf
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import logging as l
import re, requests, os
from time import sleep as s
from PyPDF2 import PdfMerger

def main(url):
	os.environ['MOZ_HEADLESS'] = '1'
	l.debug("Opening Firefox web driver...")
	driver = webdriver.Firefox(service_log_path=os.devnull)
	driver.set_page_load_timeout(10)
	l.debug("Done opening!")

	l.debug("Getting page...")
	try:
		driver.get(url)
	except TimeoutException:
		driver.execute_script("window.stop();");
	l.debug("Done getting page!")

	l.debug("Executing scroll down...")
	toScroll = driver.execute_script("""return document.getElementById("jmuse-scroller-component").scrollTopMax""")
	for i in range(0, toScroll, 10):
		driver.execute_script("""document.getElementById("jmuse-scroller-component").scrollTo(0, arguments[0])""", i)
	l.debug("Done scrolling down!")
	
	l.debug("Downloading all svgs as pdfs...")
	resources = driver.execute_script("return window.performance.getEntriesByType('resource');")
	cnt = 0
	merger = PdfMerger()
	for resource in resources:
		if len(re.findall("score", resource['name'])) == 4 and re.search("svg", resource['name']): # check for other types if needed
			l.debug(resource['name'])
			svg2pdf(bytestring=requests.get(resource['name']).text, write_to=str(cnt) + ".pdf", scale=2.0)
			merger.append(str(cnt) + ".pdf")
			os.remove(str(cnt) + ".pdf")
			cnt += 1
	l.debug("Done downloading!")
	
	l.debug("Creating pdf...")
	merger.write("sheet.pdf")
	merger.close()
	l.debug("Done creating pdf!")

	l.debug("Closing Firefox web driver...")
	driver.quit()
	l.debug("Closed Firefox web driver!")

if __name__ == "__main__":
	l.basicConfig(level=l.DEBUG)
	main(input())
