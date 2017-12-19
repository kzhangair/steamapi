#!/bin/bash
for((i=5;i<8;i++))
do
{
	awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData0${i}.csv > result_0${i}
}&
done

wait
cat result_05 result_06 result_07 > MultiNodeResult_Thumm02
