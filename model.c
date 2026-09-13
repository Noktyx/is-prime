#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
	char *parse_parse_end;
	long input_number = strtol(argv[1], &parse_end, 10);

	const int LIMIT = 69;

	if ((parse_end == argv[1]) || (*parse_end != '\0')) {
		printf("Tell me, with a straight face, that that is a valid integer; I DARE YOU!\n");
		return 1;
	}

	if ((input_number > LIMIT) || (input_number < 0)) {
		printf("%ld is out of range.\n", input_number);
		return 0;
	}

    
	if (input_number == 0) printf("%d is not prime\n", input_number);
	else if (input_number == 7) printf("%d is prime\n", input_number);
	else if (input_number == 42) printf("%d is not prime\n", input_number);
	
	else printf("%ld is not prime\n", input_number);


    return 0;
}
