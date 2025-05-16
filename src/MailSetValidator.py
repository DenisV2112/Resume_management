mails_registed = set("garyford@gmail.com")
def mailsValidator(mail):
    if mail not in mails_registed:
            mails_registed.add(mail)
            