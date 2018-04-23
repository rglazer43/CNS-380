##### Web Brute Force #####
##### CNS-380/597 Advanced Cybersecurity Automation - Ryan Haley####
'''
During your pentest you find a website that you believe to be of high value.
You decide to probe it to find any webpages it might be hiding and hopefullly
return a page with that you can use to gather contact information.

Write a script that will take in a list of file paths (you can use the txt
file provided WebPath.txt) and check them against the given website.
The script will then notify the user which link(s) were successful.

You then must scrape the webpage of any directories/files that were found and
return any phone numbers and email addresses you find on the page.

NOTE: This problem is only to be done against the given URL.
'''
#import releent libraries
import requests, re

#open WebPath file, create an object for it and set as read
fileObject = open("WebPath.txt", "r")

#create url object for website
url = 'https://www.secdaemons.org/'

#create empty list for appended url objects
urllist=[]

#use a for loop to search through each item in the list
for line in fileObject:

	#append each list path in the text doc to the url
	urllist.append(url+line.strip())

#open the output file, create an object for it and set as write 
fileWrite = open('output.txt', 'w')

#use a for loop to interate through the list of urls
for i in urllist:

	#use requests lib and GET function to attempt each potential path
	page = requests.get (i, verify = False)

	#use requests findall function and RegEx to search for all phones numbers and store in a variable. 
	phone = re.findall('\(\d{3}\) \d{3}-\d{4} | \d{3}-\d{3}-\d{4}', page.content.decode('utf-8'))

	#write any found phone numbers to the output file
	fileWrite.write(str(phone))

	#use requests findall function and RegEx to search for all email addresses and store them in a variable.
	email = re.findall('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', page.content.decode('utf-8'))

	#write any found email addresses to the output file
	fileWrite.write(str(email))

#close all open files
fileObject.close()
fileWrite.close()

