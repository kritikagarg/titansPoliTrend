#!bin/bash

IFS=$' \t\r\n'

count=1
while read -r line;

do
	#echo $count
	#echo $line
	user_id=$(echo $line | awk -v FS=, {'print $1'});
	#echo $user_id;
	date=$(./script/TimestampEstimator.py -t $user_id);
	date_up=$(echo $date|awk -v FS=. {'print $1'}|awk {'print $5" " $6'});
	echo $date_up
	echo -e $user_id"\t"$date_up>>$2
	#awk -v v1="$date" -F"," 'BEGIN { OFS = "," } {$4=v1; print}' $1 >> b.csv
	#count=$((count+1))
done<$1
