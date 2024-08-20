import re
from typing import Callable

# type Email = Callable[[str], list[str]]
get_emails = lambda text: re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
# get_emails: Email = lambda text: re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

def main() -> None:
	with open('text.txt') as txt:
		content: str = txt.read()

	print(get_emails(content))

if __name__ == "__main__":
	main()