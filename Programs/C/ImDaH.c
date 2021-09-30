#include <stdio.h>
#include <string.h>
#include "../../Libraries/C/lib.h"

void clearSTDIN() {
	char buf[1001];
	fgets(buf, 1001, stdin);
}

char *getInput(bufferLength) {
	char NEWLINE[1] = "\n";
	char buf[bufferLength];
	fgets(buf, bufferLength, stdin);
	printf("Raw is '%s'\n", buf);
	char cleaned[bufferLength];
	int cleanedIndex = 0;
	for (int i = 0; i < bufferLength; i++) {
		if (buf[i] == NEWLINE[0]) {
			printf("[NEWLINE]");
		} else {
			printf("%c", buf[i]);
			cleaned[cleanedIndex] = buf[i];
			cleanedIndex += 1;
		}
	}
	printf("\nCleaned is %s\n", cleaned);
	for (int i = 0; i < bufferLength; i++) {
		printf("[%c]", cleaned[i]);
	}
	clearSTDIN();
	return(cleaned);
}

int main() {
	int done = 0;
	while (done == 0) {
		system("pwd");
		printf("\nActions:\n(0): Write a message.\n(1): Read a message.\n(2): Clear messages.\n(3): Quit.\n:");
		char action;
		char actions[5] = "01234";
		scanf(" %c", &action);
		getchar();
		printf("%c\n", action);
		if (action == actions[0]) {
			encode();
		} else if (action == actions[1]) {
			decode();
		} else if (action == actions[2]) {
			strip();
		} else if (action == actions[3]) {
			done = 1;
		} else if (action == actions[4]) {
			system("ls");
			done = 1;
		}
	}
	return(0);
}