from typing import List


# One might argue to go for Euler's sieve, but I personally reckon that, for this use case, Eratosthenes' sieve is better...
# But, hey, might change idea and implement the former, too; not like it should be *that* hard in Python...
def sieve_of_eratosthenes(limit: int) -> list:
	"""Returns a list of all prime numbers from 0 to whatever specified.

	Args:
		limit (int)

	Returns:
		list: A list of all the prime numbers from 0 to the specified integer.
	"""
	if (limit < 0):
		limit *= -1
		print("Negative limit has been converted to its opposite number.")


	print(f"\nStarting sieve with limit: {limit}")
	is_prime: List[bool] = [True] * (limit + 1)
	
	for current_num in range(2, (int(limit**0.5) + 1)):	#Check each number except integers bigger than the square root of the limit
														#since they would only lead to numbers bigger than the limit itself, hence making them useless.
		if is_prime[current_num]:
			for multiple in range((current_num**2), (limit + 1), current_num):  #Remove the multiples of 'current_num' if prime, starting from its square
																				#to avoid doing work that has already been done.
				is_prime[multiple] = False


	list_of_primes: List[int] = [num for num in range(2, limit + 1) if is_prime[num]]
	# ^^^ Funnily enough, this means that 'is_prime[0]' and 'is_prime[1]' remain 'True',
	# but when putting together the final list they are skipped anyway, so... Cool, I suppose!
	print(f"{len(list_of_primes)} primes found.")
	# print(list_of_primes)
	
	return (list_of_primes)
