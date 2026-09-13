from packages.sieve_prime_numbers import sieve_of_eratosthenes
from utils.helpers import ask_yes_no


def main() -> bool:
	try:
		change_var_name: int = int(float(input("[PLACEHOLDER]: "))) #FIXME: Better input text
		sieve_of_eratosthenes(change_var_name)

	except ValueError:
		print("Your input was not a valid number.")
		return (False)

	except Exception as error:
		print("Exception raised while attempting to parse your input:", error)
		return (False)


	return (True)


if __name__ == "__main__":
	main()
