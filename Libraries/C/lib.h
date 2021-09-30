#include <stdlib.h>
#include <errno.h>
#include <string.h>

char *getFileName(int maxLength) {
	char filename[maxLength];
	printf("Filename:");
	for (int i = 0; i < maxLength; i++) {
		char c = getchar();
		filename[i] = c;
	}
	printf("Filename: %s\n", filename);
	return(filename);
}

int encode() {
	unsigned int filenameLength;
	scanf("%u", &filenameLength);
	printf("Length: %u\n", filenameLength);
	char filename[11];
	for (int i = 0; i < strlen(filename); i++) {
		filename[i] = NULL;
	}
	printf("Filename:");
	for (int i = 0; i < 11; i++) {
		char c = getchar();
		filename[i] = c;
	}
	char *choppedFilename;
	choppedFilename = malloc(sizeof(char) * strlen(filename)-1);
	for (int i = 0; i < strlen(choppedFilename); i++) {
		choppedFilename[i] = NULL;
	}
	strcpy(choppedFilename, filename);
	for (int i = 0; i < strlen(choppedFilename); i++) {
		printf("[%c]", choppedFilename[i]);
	}
	printf("\n");
	printf("Chopped filename: [%s]\n", choppedFilename);
	printf("Filename: %s\n", filename);
	printf("Encoding...\n");
	printf("%s\n", filename);
	FILE *file = fopen(filename, "w");
	if (file == NULL) {
		printf("Error: %s\n", strerror(errno));
		return(1);
	}
	fclose(file);
}

void decode() {
	/*getFileName(11);*/
	printf("Decoding...\n");
}

void strip() {
	/*getFileName(11);*/
	printf("Stripping...\n");
}