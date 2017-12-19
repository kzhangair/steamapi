#!/bin/bash
awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData01.csv > result_01 &

awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData02.csv > result_02 &

awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData03.csv > result_03 &

awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData04.csv > result_04 &

wait
cat result_01 result_02 result_03 result_04 > MultiNodeResult_Thumm01
