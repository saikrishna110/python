"""
Assignment-3:
WAP to print 'Hi' on the screen
and 'I Love Python' to the file using the print function
"""
fp=open('src1.txt', 'w')
fp.write("hi i love python")
fp.close()
print("hi i am new to python",file=open('src.txt','w'))