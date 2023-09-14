#!/bin/bash
#check if th file is exist or not
printf  "please enter the name of the file, if u want exit enter -1\n"
read filename
while [ ! -e $filename  ]
do
	printf "the file does not exist please enter the file name again or -1 to exit from the program\n"
	read filename
if [ $filename -eq "-1" ]
then
	printf "Good Bye\n"
	sleep 2
	exit -1
fi
done
#loop for the menu for usier to chose from it
while true
do
printf "\n\n\t****welcome to contact manegment system****\n\n
        \t\tMAIN MENU\n
        ==============================================\n
        [1]Add new contact
        [2]List all the contact
        [3]Search for contact 
        [4]Edit a contact 
        [5]Delete a contact
        [0]exit from the program\n
        ==============================================\n
        Enter the choice : \n"
read choice
#if the choice equal to zero then exit from the prohram
if [ $choice -eq 0 ]
then
printf "bye bey :):)\n\n"
	exit 0
#check if the coice is valid 
elif [ $choice -lt 1 -o  $choice -gt 5 ]
then
	printf " You should enter number from 0-5 \n"
	continue 
#Add a new contact
elif [ $choice -eq 1 ]
then
	#ask to enter the first name
	printf "Enter First Name: \n"
	read firstname
	#ask for the numbers of phone number that the user want to enter
	num=""
	printf "How much phone u want to enter \n"
	read count
	for (( i=0 ; i < count ; i++ ))
	do
	
		while true
		do
			#check if the number is already in the file
			printf " enter the %d phone \n" $((i+1))
			read n
			cut -d',' -f3 $filename | grep "\<$n\>" > /dev/null 
			u=$?
			if [[ u -eq 0 ]]
			then 
			printf "the number you enter is already in the file,please enter valid one\n\n"
			continue
			fi
			#check if the number is only digits and 9 or 10 digits only
			if echo $n | grep "\<[0-9]\{9,10\}\>" > /dev/null
			then
				if [ $i -eq $((count-1)) ]
				then
					num+=$n
					break
				else
					num+=$n
					num+=";"
					break
				fi
			else
				printf " u should enter correct number with 9 or 10 digits \n"
				continue
			fi
		
		done
	done
	
	email="0"
	printf " if u want enter an email write 1, else -1\n"
	read c
	if [ $c -eq 1 ]
	then
		while true
			do
				#ask to enter the email
				printf " enter the email \n"
				read em
				#hceck if the email is already in the file
				cut -d',' -f4 $filename | grep "\<$em\>" > /dev/null 
				u=$?
				if [[ u -eq 0 ]]
				then 
				printf "the email you enter is already in the file,please enter valid one\n\n"
				continue
				fi
				#check the validation of the email
				if echo $em | grep ".*@.*" > /dev/null
				then
					email=$em
					break
				else
					printf "you should enter correct email\n"
					continue
				fi
				
			done
	else
		:
	fi
	#ask to enter the las name
	lastname="0"
	printf " if u want enter an last name write 1, else -1\n"
	read c
	if [ $c -eq 1 ]
	then
		printf " enter the last name \n"
		read nm
		lastname=$nm
	else
		:
	fi
	
			
	printf "%s, %s, %s, %s\n" $firstname $lastname $num $email >> $filename
	printf "\n\nthe file after adding the new contact is : \n\n"
	cat $filename
	
fi
#check if the file is embty to prevent the user from using the other options
a=$(wc -l $filename | cut -d' ' -f1)
if [[ a -eq 1 ]]
then 
printf "the file is embty\n\n"
else
#choice 2 is to list the contact
if [ $choice -eq 2 ]
then
	#delete the first line from the input file and sent it to temp
	sed  "1d" $filename > temp
	#convert the , to spaces
	tr ',' ' ' < temp > temp1 
	#remove the consecuntive spaces
	tr -s ' ' ' ' < temp1 > temp
	#coice 1 is to sort by name and 2 is to sort by the last name 
	printf " sort by first name: 1, sort by last name: 2\n"
	read so
	if [ $so -eq 1 ]
	then
		sort -k 1 < temp > temp1 
		cat temp1 > temp
		one=1
		two=1
		three=1
		four=1
		#let the user chose the fields he want to print with the first name
		printf " if u want last name enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			two=2
		fi
		printf " if u want numbers enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			three=3
		fi
		printf " if u want email enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			four=4
		fi
		printf "\n\nthe sorted contact by the first name is : \n\n"
		cut -d' ' -f$one,$two,$three,$four temp 
		
	elif [ $so -eq 2 ]
	then
	#let the user chose the fileds he want to print with the last name
		sort -k 2 < temp > temp1 
		cat temp1 > temp
		one=2
		two=2
		three=2
		four=2
		
		printf " if u want first name enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			one=1
		fi
		printf " if u want numbers enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			three=3
		fi
		printf " if u want email enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			four=4
		fi
		printf "\n\nthe sorted contact by the last name is : \n\n"
		cut -d' ' -f$one,$two,$three,$four temp 
		
	
	else
		printf " wrong choice [1-2] \n"
	
	fi 
#search for the contact 
elif [ $choice -eq 3 ]
then
	f=""
	s=""
	t=""
	fo=""
	#chose which fields the user want to search 
		printf " if u want search first name enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			printf " enter the first name:\n"
			read f
		
		fi
		printf " if u want search last name enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			printf " enter the last name:\n"
			read s
		
		fi
		printf " if u want search numbers enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			printf " enter the number:\n"
			read t
		
		fi
		printf " if u want search email enter 1, else -1\n"
		read h
		if [ $h -eq 1 ]
		then
			printf " enter the email:\n"
			read fo
		fi
		#if the user does not chose any field then the program will print error messege
		if [ "$f" == "" ] && [ "$s" == "" ] && [ "$t" == "" ] && [ "$fo" == "" ]
		then
		printf "please enter one or more fildes you wnat to search\n"
		else 
		#search for the fields chosen by user above
	                printf "\nthe result is : \n\n"	
			grep .*"$f".*"$s".*"$t".*"$fo".* $filename || printf " It not exist \n"
			printf "\n\n"
		fi
		f=""
		s=""
		t=""
		fo=""
#edit a contact info
elif [ $choice -eq 4 ]
then
#delete the first line from the file name and move the result to temp
	sed  "1d" $filename > temp
	tr ',' ' ' < temp > temp1 
	tr -s ' ' ' ' < temp1 > temp
	cat -n temp
	printf "\n\n"
	#let the user chose the contact he want to edit it 
	printf "enter which contact you want to change\n"
	read l
	
	#let the user chpse the field he want to edit it
	printf "enter which field u want to change\n"
	printf "1.first name\n2.last name\n3.phones number\n4.email\n"
	read ch
	#get the line of the contact the user want to edit
        o=$(echo $(sed -n $((l))p temp) | cut -d' ' -f$((ch)))
        (echo $(sed -n $((l))p temp) | tr ' ' '\12' > temp3)
	printf "please enter the new value for the field\n"
	new=""
	#check if the user want to edit the mobile number for validation 
	if [ $ch -eq 3 ]
	then
	
		printf "How much phone u want to enter \n"
		read count
		for (( i=0 ; i < count ; i++ ))
		do
		
			while true
			do
				
				printf " enter the %d phone \n" $((i+1))
				read n
				cut -d',' -f3 $filename | grep "\<$n\>" > /dev/null 
				u=$?
				if [[ u -eq 0 ]]
				then 
				printf "the email you enter is already in the file,please enter valid one\n\n"
				continue
				fi
				if echo $n | grep "[0-9]\{9,10\}" > /dev/null
				then
					if [ $i -eq $((count-1)) ]
					then
						new+=$n
						break
					else
						new+=$n
						new+=";"
						break
					fi
				else
					printf " u should enter correct number with 9 digits \n"
					continue
				fi
			
			done
		done
	#check if the user want to edit the email for validation 
	elif [ $ch -eq 4 ]	
	then
		
		while true
			do
				printf " enter the email \n"
				read new
				cut -d',' -f4 $filename | grep "\<$new\>" > /dev/null 
				u=$?
				if [[ u -eq 0 ]]
				then 
				printf "the email you enter is already in the file,please enter valid one\n\n"
				continue
				fi
				if echo $new | grep ".*@.*" > /dev/null
				then
					break
				else
					printf "you should enter correct email\n"
					continue
				fi
				
			done
	else
	#read the new value
		read new
	fi
	y=$(wc -l temp | cut -d' ' -f1)
	echo $y
	#put the edited contact in the same place as old and delete the old one
	if [[ $((l)) -eq $y ]]
	then 
		printf "\n" >> filename
	   	sed -i "$ch s/$o/$new/g" temp3
	   	sed -i $((l+1))d $filename
	   	sed "$((l+1)) i "$(paste -s -d',' temp3)"" $filename > temp4 
	   	grep -v '^[[:space:]]*$' temp4 > y 
	   	cat y > temp4
   	else 
	   	sed -i "$ch s/$o/$new/g" temp3
	   	sed -i $((l+1))d $filename
	   	sed "$((l+1)) i "$(paste -s -d',' temp3)"" $filename > temp4  
   	fi
   	
   	cat temp4 > $filename
   	printf "\n\nthe file after editing : \n\n"
   	cat $filename
   	printf "\n\n"
#delete contact info from the file
elif [ $choice -eq 5 ]
then
#delete the first line from input file and let the useer chose which he want to delete
	cat $filename | sed 1d > temp 
	cat -n temp
	printf "\nenter whice contact you want to delete \n"
	read line
	#delete the contact
	sed $((line+1))d $filename > temp
	cat temp > $filename
	printf "\n\nthe file after deleting the contact : \n\n"
	cat $filename
	printf "\n\n"
fi
fi
done
