#include <stdio.h>
#include <string.h>

void checkPassword(char password[]);
void expand(char s1[]);

int main(){
	char password[] = "Aqw2@";
	checkPassword(password);
	char s1[] = "0-9";
	expand(s1);
}		

//////////////////// chaks if password is strong /////////////////////////
void checkPassword(char password[]){
	int minLenght = 5;
	int passLength = strlen(password);
	int ifStrong = 0;
	int i;

	if (passLength >= minLenght)
		ifStrong += 1;	
	
	//capital ?
	for (i = 0; i < passLength; i++){
		if (password[i] >= 65 && password[i] <= 90){ 
			ifStrong += 1;
			break;
		}	
	}
	
	//!#%@ ?
	for (i = 0; i < passLength; i++){
		if (password[i] == 33 || password[i] ==  35 || password[i] ==  37 || password[i] ==  64){
			ifStrong += 1;	
			break;
		}
	}
	
	//number ?	
	for (i = 0; i < minLenght; i++){	
		if (password[i] >= 48 && password[i] <= 57){
			ifStrong += 1;	
			break;
		}			
	}
	
	if (ifStrong > 3) printf("Your password is strong (: \n");
	else printf("Your password is strong %d of 4:\n ", ifStrong);	
}
///////////////////////////////////////////


void expand(char s1[]){
	int i;
	int start = s1[0];
	int end = s1[2];
	
	for (i = start; i <= end; i++){
		printf("%c," ,i);
	}
	printf("\n");		
}

	
