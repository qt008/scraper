#!/usr/bin/env python3
import csv
import requests
from requests_html import HTMLSession

# Scrape contents from a website and save scraped data in a csv file.
# This scrape script focuses on contents scraped from multiple pages differentiated by a pagination number

# store contents in here
csv_file = open('cont1_.csv', 'w')
#A name, label or heading for the contents being stored
# fieldnames = ['contacts']
#create  a variable to handle all csv actions into this file
csv_writer = csv.writer(csv_file)
#Write your first content into the csv file which is the field name contacts
csv_writer.writerow(['contacts'])

# call the HTMLSession class responsible for all our scraping functions
session = HTMLSession()
# number of pages to loop through
z = 10000
# run a FOR loop to go through all the the pages available 
for c in range(z):
	# This is a dummy page but you should replace with an authentic one
	r = session.get('https://localhost/scraping-course/ads?by_paying_member=0&sort=date&order=desc&buy_now=0&urgent=0&page='+str(c+1))

	# Fetch the needed css class for identification of the scraping target 
	sources = r.html.find('.gtm-ad-item')
	# Run another FOR loop to figure out if the links contain specific external links necessary for our main scraping target
	for linking in sources:
		link_found = linking.absolute_links
		# once a link is found run LOOP through it for find the scraping target
		for getting in link_found:
			try:
				# Try to find out if the URL contains a keyword 'AD'
				if getting.find('ad') > 0 :
					# once we confirm that then we visit that page and continue with our scraping target search
					x = session.get(getting)
					# now that we are finally on our desired scraping page we need to get the exact css of the scraping target we desire
					sources2 = x.html.find('.number--12hbs',first=True)
					# fetch the text content of that target which will be our desired result
					contact = sources2.text
					# print the content out whiles running the script
					print(contact)
					# write the content into our csv file initiated in the beginning
					csv_writer.writerow([contact])

			except Exception as e:
				print('none')
# close all csv connections
csv_file.close()
			
			
