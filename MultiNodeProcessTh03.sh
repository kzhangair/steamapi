#!/bin/bash
awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData08.csv > result_01 &

awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData09.csv > result_02 &

awk -F '\v' 'BEGIN{min = 200000;max = -1;RS = "\a"} {if($1<min){min = $1}if($1>max){max = $1}} END{printf("%d %d\n", min, max)}' cleanedData10.csv > result_03 &


wait
cat result_01 result_02 result_03 > MultiNodeResult_Thumm03
