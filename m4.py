from secrets import choice
from string import ascii_letters, digits, punctuation
from typing import Callable

pass_gen: Callable[[int], str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))

def main() -> None:
	print(pass_gen(10))
	print(pass_gen(30))
	print(pass_gen(5))
	print(pass_gen(9))

if __name__ == "__main__":
	main()