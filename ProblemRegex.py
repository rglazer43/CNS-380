##### Problem #####
##### CNS-380/597 - Ryan Haley####

#Ryan Glazer (1803117) 03/30/2018
#CNS-380: Week 2: Homework #1

#Write a regular expression to fit the following:

#1 Phone number in the format of
#  xxx-xxx-xxxx

#	\d{3}-\d{3}-\d{4}

#2 Phone number in the format of
#  (xxx) xxx-xxx

#	\(\d{3}\) \d{3}-\d{4}


#3 Phone number in the format of
#  +x xxx.xxx.xxxx

#	\+\d{1} \d{3}\.\d{3}\.d{4}


#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx

#	\d{3}-\d{2}-\d{4} |\d{9}
