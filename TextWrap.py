import textwrap

"""S=input()
n,c=int(input()),1
for i in S:
	if c==n:
		print(i,end='\n')
		c=1
	else:
		print(i,end='')
		c+=1"""

def wrap(string, max_width):
	return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


"""
Textwrap
The textwrap module provides two convenient functions: wrap() and fill().
textwrap.wrap() 
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
It returns a list of output lines.
textwrap.fill() 
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph. 
"""