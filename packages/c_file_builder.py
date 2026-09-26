from typing import List


def build_c_code_header(limit: int) -> List[str]:
	lines: List[str] = []

	lines.append("#include <stdio.h>")
	lines.append("#include <stdlib.h>")
	lines.append("\n")
	lines.append("int main(int argc, char *argv[]) {")
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
	lines.append("\t\tprintf(\"%ld is out of range...\\n\", input_number);")
	lines.append("\t\treturn 0;")
	lines.append("\t}")
	lines.append("\n")


	return (lines)


def build_c_code_logic(limit: int, primes: List[int], hardcode_non_primes: bool = True) -> str:
	lines: List[str] = build_c_code_header(limit)
	prime_set: set = set(primes)

	if (hardcode_non_primes):
		lines.append(f"\tif (input_number == 0) printf(\"%ld is not prime\\n\", input_number);")
		for num in range(1, (limit + 1)):
			prime_state: str = "prime" if (num in prime_set) else "not prime"
			lines.append(f"\telse if (input_number == {num}) printf(\"%ld is {prime_state}\\n\", input_number);")
	
	else:
		lines.append(f"\tif (input_number == {primes[0]}) printf(\"%ld is prime\\n\", input_number);")
		for prime in primes[1:]:
			lines.append(f"\telse if (input_number == {prime}) printf(\"%ld is prime\\n\", input_number);")
		lines.append("")
		lines.append("\telse printf(\"%ld is not prime\\n\", input_number);")

	lines.append("")
	lines.append("\treturn 0;")
	lines.append("}")
	lines.append("")

	return ("\n".join(lines))




if __name__ == "__main__":
	print("Using a sample to test this script.\n\n")
	print(build_c_code_logic(11, [2,3,5,7,11], True))
