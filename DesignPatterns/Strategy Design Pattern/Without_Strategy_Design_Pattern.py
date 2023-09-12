class PasswordGenerator:
    def generate_password(self, password_type='alpha'):
        if password_type == 'alpha':
            return "abcdefghijklmnopqrstuvwxyz"
        elif password_type == 'numeric':
            return "1234567890"
        else:
            return "abcde12345"


if __name__ == "__main__":
    pg = PasswordGenerator()
    password = pg.generate_password(password_type='numeric')
    print("Your generated password is - ", password)
