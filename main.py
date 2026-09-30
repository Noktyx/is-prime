import os, random
from typing import Final

from packages.sieve_prime_numbers import sieve_of_eratosthenes
from packages.c_file_builder import build_c_code_logic
from utils.helpers import ask_yes_no, ask_file_name, clear_terminal


def main() -> bool:
	DEFAULT_FILE_NAME: Final[str] = random.choice(["homework", "output", "uwu", "furry_gay_porn_video_player_free_novirus"]) #I'm such a corny git, omG
	
	try:
		limit: int = int(float(input("Enter the upper limit for prime search: ")))
		to_hardcode_non_primes: bool = ask_yes_no("Hardcode non-prime numbers, too? (If not, only primes will be hardcoded)")
		to_hardcode_numbers_in_print: bool = ask_yes_no("Hardcode the corresponding number itself in each printf instead of using %ld?")
		clear_terminal()
		file_name: str = ask_file_name(DEFAULT_FILE_NAME, ".c")
		
		primes: list = sieve_of_eratosthenes(limit)
		c_source: str = build_c_code_logic(limit, primes, to_hardcode_non_primes, to_hardcode_numbers_in_print)
		
		with open(file_name, "w") as output_file:
			output_file.write(c_source)

		print(f"C file written to \"{os.path.abspath(file_name)}\"")


	except ValueError:
		print("Your input is not a valid number.")
		return (False)


	except Exception as error:
		print("Exception raised while attempting to parse your input: ", error)
		return (False)


	return (True)


if __name__ == "__main__":
	main()
