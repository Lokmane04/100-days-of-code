from bs4 import BeautifulSoup

try:
    # you have an error when you take the courses , just add encoding='utf-8' in the open(\\) function
    with open("website.html", encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print("The file 'website.html' does not exist in the current directory.")
    exit(1)
except UnicodeDecodeError:
    print("The file 'website.html' contains characters that are not supported by the 'utf-8' encoding.")
    exit(1)

soup = BeautifulSoup(content, "html.parser")

if soup.title is not None:
    print(soup.title)
else:
    print("The HTML document does not have a <title> tag.")
