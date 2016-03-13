#include "stdio.h"
#include "string.h"
#include "ctype.h"

int main(int argc, char** argv){

int i = 0;
printf("Read in: ");
while(argv[1][i] != '\0'){
	putchar(argv[1][i]);
	i++;
}
putchar('\n');

if(argc < 2){
	printf("Usage: atbash <string>\n\n");
	return -1;
}
else{
	printf("Encoding your string...\n");
	for(int j = 0; j<i; j++){
		char temp = argv[1][j];
		//filter out non-alphas
		if(temp < 65){
			putchar(temp);
		}
		else if(temp > 122){
			putchar(temp);
		}
		else if(temp < 97 && temp > 90){
			putchar(temp);
		}
		else{
			temp = tolower(temp);
			putchar(122-(temp%97));
		}
	}
	putchar('\n');
}
return 0;
}
