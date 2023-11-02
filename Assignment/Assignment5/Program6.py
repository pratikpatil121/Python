'''
# # # # # 
@ @ @ @ @
# # # # #
@ @ @ @ @
# # # # #
'''

for i in range(5):
	for j in range(5):
		if i%2==0:
			print("#",end=" ")
		else:
			print("@",end=" ")

	print()
