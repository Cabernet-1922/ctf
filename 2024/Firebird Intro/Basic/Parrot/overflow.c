#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>


char flag[33];

int main(int argc, char * argv[]){
	setbuf(stdout,NULL);
	int value_check = 0;
	char buf[250];
	int setid_result;
	gid_t gid = getegid();
	setid_result = setresgid(gid, gid, gid);


	FILE *f = fopen("flag.txt", "r");
	if (f == NULL) {
		printf("Flag file is missing");
		exit(0);
	}
	
	fgets(flag, 33, f);

	printf("Type something and I'll repeat it to you, but I can't remember too many things... \n");
	gets(buf);

	printf("%s \n", buf);
	if (value_check > 0){
		printf("%s\n", flag);
	}


}



