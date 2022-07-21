#!/bin/bash
true=✅
false=❌
yol="./function"
name=$(basename $1 .c) 
you_output="${name}_output.txt"
true_output="${name}_true.txt"

gcc test_codes/test_${name}_main.c $yol/${name}.c
./a.out > outputs/${name}_output.txt
diff outputs/${name}_true.txt outputs/${name}_output.txt > /dev/null

if [ $? -eq 0 ];then
	tput setaf 2						
	printf "%-30s %s\n" $name $true 
	tput sgr0						
else
	tput setaf 1						
	printf "%-30s %s\n" $name $false	
	tput sgr0							
	python3 kod.py outputs/$you_output outputs/$true_output
fi

rm -rf outputs/${name}_output.txt
rm -rf a.out