def getpass(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    password = ''
    while True:
        c = getch()
        if c == '\r':
            sys.stdout.write('\n')
            sys.stdout.flush()
            return password
        password += c
        sys.stdout.write('*')
