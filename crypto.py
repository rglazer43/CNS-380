#Ryan Glazer (1803117) CNS-380: Crypto Homework
#import the base64 function library
import base64

#xor function signature intakes two variables; s1 and s2.
def xor(s1,s2):
	#local variable output is converted to a string via the str() function. 
	output = str()
	#for loop creates iterative variable i and uses it to search through the length of s1.
	for i in range(len(s1)):
		#variable output is appended with the result of s1 mod s2, the functions 
		#chr() and ord() are used for string/integer/unicode conversion.
		output += chr(ord(s1[i])^s2[i])
	#return statement returns the value stored in output.
	return output

#global variable ciphertext base64 decodes the provided assignment ciphertext. 
ciphertext = base64.b64decode("MQQECVsADQAcOlMaVBUcHCoFAzpfVRoEBl0NAg4QWwMNCk4rG0kXAAIff08bOhYbQx8aCQcCEkZSfiMXATJUHRwEBwF/EwAoFgdPSwcVAxVBBBoaRRYLOlQAAEEPHzNHRysWEA1LBxQSDQ8UWl1vMgY6GkkACQsBOkAcfxYDCgdTEghMFQ8eVAQRGj4XAn44AQZ/BA4xUwcGGAddDQIOEBIaAkUaNxEQVAYBB38eACoBVQEKEBZsLwASCBFFEgY6GkkACQtTKAgdMxdVDQ4WGRVMCQIJGwAWTjAaSQQAGgEwC2ULFhANSwcUEg0PFFdUAgpPVSAMEQ9OBzYTDjEAWUMMHFxsOwgTE1QRDQs2BkkHFB4WLUcfMAQQERhfXRIEBB5bAQsMGjpUQQAECx1/EwYrEhsQSlp3KAkXAglUCAAafxVJAggCHz4OAX8HHQIfUwkOCRhHFx0OAAp/XB0RBABTKw4bPh0GQkJ5KQ4JGEccGxFFGjcRSRYAClM4EhYsUxoNSwcVA0wTEhV+MQ0LJlQHERcLAX8UGzADVRYFBxQKTBUPHlQPCgx/EwwAEk4XMAkKVTAUFhgWXREEBAlbAA0ATigbGxgFThosRwMwABwNDFMcCgBBBBQaERcBM349EQQAUysOGz4dBk9LFBJHZjUCHhpFEQcrFQcHTU4UMEZlFhVVGgQGD0YEBAYJAEUMHX8WBRUCBV9/HgAqUxcGHwcYFEwWBg8XDUUBKgBjLQ4bUzwGATEcAUMOAB4HHARHDxwARRo6FQR+NgYWMUcbNxYMQwgSCQUEQR4UAUlFGjcRGxFBGRwxQBt/ERBDCh0ERggOEhkAbzwBKlMfEUEMFjoJTz0WFBcOHV0EFUETExFFEQs6Ghp+IwsSKwIBfxEMQx8bGEYYBAIVB28xQzpZDFkPT1MrSiZyB1gCRh1QFU1BEx4RC0UaNgAIGhJPUzMCG3gAVQQEUncyQQRKHlkLRE4rWSBZFUMScglCLFJVFw4WE0YYCBMaGhZETjMRHVMSThQwRmULXhBODl4TR0wVSjJZEUgPchpEB0BOBzoCAX8HHBcKHQ5HTA0CD1MWRQkwVWMgTAteOkoBflMBTiJeCUsNTAlWB0RFGjoRB1QVBwc+CRx+UxkGH1QORgsORnEjDQAAfwABERMLVCxHCikaGUMEHV0SBARHGgARBA00fjAbFE4QPglPLRYGF0sYEwkbCAkcVBENCyZUDhsVTgowEh1/ERQAAHk+BxkSAlsDDQAAfwABEUEZHC0LC38dEAYPAF0OCRMIHgdFCgB/BAgAEwEfVTMKOh1VFwIHHAgfTUccG0RvOjoRB1QVBwc+CRxzUxIMSnkyCAlNRw8DCklOKxwbEQRCUzkIGi1fVQQEUncyCQQJWwAMEQ8xB0g=")
#global variable plaintext is initialized to the string given in the assignment hint. 
plaintext = ("When they catch you, there won't be any doubt")

#for loop initializes the iterative variable i and iterates through 
#the entire length of the ciphertext, incrementing by one (length of plaintext).
for i in range(len(ciphertext)):
	#local variable ctext is set to the exact length of the global variable plaintext 
	#and is used to iterate through the ciphertext in equal segments. 
	ctext = ciphertext[i:i+len(plaintext)]
	#local variable output runs the plaintext and ctext variables through the xor function.
	output = xor(plaintext,ctext)
	#if statement checks the output for the string value "flag" and executes if found.
	if "flag" in output:
		#print statement prints the vaule in output if the if condition is met.
		print(output)
#finished 
