from packages.sieve_prime_numbers import sieve_of_eratosthenes
from packages.c_file_builder import build_c_code_logic
from utils.helpers import ask_yes_no


def main() -> bool:
	try:
		limit: int = int(float(input("Enter the upper limit for prime search: ")))
		hardcode_non_primes: bool = ask_yes_no("Hardcode non-prime numbers, too? (If not only primes get hardcoded; rest falls to else)")
		
		primes: list = sieve_of_eratosthenes(limit)
		c_source: str = build_c_code_logic(limit, primes, hardcode_non_primes)

		with open("output.c", "w") as output_file:
			output_file.write(c_source)

		print("C source file written to: output.c")


	except ValueError:
		print("Your input was not a valid number.")
		return (False)


	except Exception as error:
		print("Exception raised while attempting to parse your input:", error)
		return (False)


	return (True)


if __name__ == "__main__":
	main()
