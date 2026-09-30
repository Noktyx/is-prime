from typing import List


def build_c_code_header(limit: int) -> List[str]:
	lines: List[str] = []

	lines.append("#include <stdio.h>")
	lines.append("#include <stdlib.h>")
	lines.append("\n")
	lines.append("int main(int argc, char *argv[]) {")
	lines.append("")
	lines.append("\tif (argc < 2) {")
	lines.append("\t\tprintf(\"Usage: %s <number>\\n\", argv[0]);")
	lines.append("\t\treturn 1;")
	lines.append("\t}")
	lines.append("")
	lines.append("\tchar *parse_end;")
	lines.append("\tlong input_number = strtol(argv[1], &parse_end, 10);")
	lines.append("")
	lines.append(f"\tconst int LIMIT = {limit};")
	lines.append("")
	lines.append("\tif ((parse_end == argv[1]) || (*parse_end != '\\0')) {")
	lines.append("\t\tprintf(\"Tell me, with a straight face, that what you just entered is a valid integer; I DARE YOU!\\n\");")
	lines.append("\t\treturn 1;")
	lines.append("\t}")
	lines.append("")
	lines.append("\tif ((input_number > LIMIT) || (input_number < 0)) {")
	lines.append("\t\tprintf(\"%ld is out of range... D:\\n\", input_number);")
	lines.append("\t\treturn 0;")
	lines.append("\t}")
	lines.append("\n")


	return (lines)


def build_print_statement_helper(number: int, state: str, to_hardcode_number: bool) -> str:
	if (to_hardcode_number): return f"printf(\"{number} is {state}\\n\");"
	else: return f"printf(\"%ld is {state}\\n\", input_number);"


def build_c_code_logic(limit: int, primes: List[int], to_hardcode_non_primes: bool = True, hardcode_numbers_in_print: bool = False) -> str:
	lines: List[str] = build_c_code_header(limit)
	prime_set: set = set(primes) #hashing goes vroooooooooooooom

	if (to_hardcode_non_primes):
		lines.append(f"\tif (input_number == 0) {build_print_statement_helper(0, 'not prime', hardcode_numbers_in_print)}")
		for number in range(1, (limit + 1)):
			prime_state: str = "prime" if (number in prime_set) else "not prime"
			lines.append(f"\telse if (input_number == {number}) {build_print_statement_helper(number, prime_state, hardcode_numbers_in_print)}")

	else:
		if (primes):
			lines.append(f"\tif (input_number == {primes[0]}) {build_print_statement_helper(primes[0], 'prime', hardcode_numbers_in_print)}")
			for prime in primes[1:]:
				lines.append(f"\telse if (input_number == {prime}) {build_print_statement_helper(prime, 'prime', hardcode_numbers_in_print)}")
			lines.append("")
			lines.append("\telse printf(\"%ld is not prime\\n\", input_number);")  #Unknown number here, therefore, obviously, %ld must stay.
		
		else: #Basically just 0 and 1
			lines.append("\tprintf(\"%ld is not prime\\n\", input_number);")

	lines.append("")
	lines.append("\treturn 0;")
	lines.append("}")
	lines.append("")


	return ("\n".join(lines))




if __name__ == "__main__":
	print("Using a sample to test this script.\n\n")
	print(build_c_code_logic(11, [2,3,5,7,11], True))
