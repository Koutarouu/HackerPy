import re

def fun(s):
    # return True if s is a valid email, else return False
    try:
    	name=s.split("@")[0]
    	website=s.split("@")[1].split(".")[0]
    	ext=s.split("@")[1].split(".")[1]
    except IndexError as e:
    	return False
    if name.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif not website.isalnum():
        return False
    else:
    	return True and lx=0<len(ext)<=3    	

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)