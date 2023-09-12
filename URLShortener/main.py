import pyshorteners


def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)


def main():
    print("Welcome to the URL Shortener!\n")

    long_url = input("Enter the long URL you want to shorten: ")
    shortened_url = shorten_url(long_url)

    print(f"\nShortened URL: {shortened_url}")


if __name__ == "__main__":
    main()
