%{
	int counter = 0;
%}
letter [a-zA-Z]

%%

{letter}+ {printf("input is a word\n"); counter++;}

%%
main() {
	yylex();
	printf("\nThere are total %d words\n",counter);
}
