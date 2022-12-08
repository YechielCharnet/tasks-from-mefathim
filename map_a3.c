#include <stdio.h>
#include <string.h>

int isPalindrome(char str[], int startFrom, int n);


int main(){
	char str[] = "wturtw";
	int n = strlen(str)-1;
	int startFrom = 0;
	printf("%d\n", isPalindrome(str, startFrom, n));
}


int isLetter(char* s){
	if ((s < 65 || s > 90) && (s < 97 || s > 122))
		return 0;
	if (s >= 65 && s <= 90)
		s = s+32;
	return 1;
}
	
int isPalindrome(char str[], int startFrom, int n){
	int checkIfPalindrome = 1;
	if ((checkIfPalindrome) && (n > startFrom)){
		if (isLetter(&str[startFrom])
		if (str[startFrom] == str[n]){
			checkIfPalindrome = isPalindrome(str, startFrom+1, n-1);
		}
		else checkIfPalindrome = 0;
	}
	return (checkIfPalindrome);
}



