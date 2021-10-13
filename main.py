"""
This program is designed for a specific job https://github.com/ProgrammerAkosh/Working_on_numbers_in_Python
"""
ln_juft = []
ln_toq = []

n = int(input("n : "))

for i in range(1 , n + 1):
	if (i % 2 == False):
		ln_juft.append(i)
	elif (i % 2):
		ln_toq.append(i)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Juft sonlar~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(ln_juft)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Toq sonlar~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(ln_toq)
# Akosh...