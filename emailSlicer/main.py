def main():
    print('Welcome to email slicer')
    print("")

    input_email = input('Please enter your email address: ')

    (email_name, email_domain) = input_email.split('@')
    (email_domain, email_extension) = email_domain.split('.')

    print('Your username is: ' + email_name)
    print('Your domain is: ' + email_domain)
    print('Your extension is: ' + email_extension)
    print("")
    print('Thank you for using email slicer')

main()
