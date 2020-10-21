import re,email.utils

def validate_email_addr(n):
    for i in range(n):
        mail = input("Email "+str(i+1)+": ")
        addr = email.utils.parseaddr(mail)[1]
        if re.search(r"^[a-zA-Z][a-zA-Z0-9-\._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$",addr):
            return mail

if __name__ == "__main__":
    n = int(input("Number of Emails: "))
    print(validate_email_addr(n))


