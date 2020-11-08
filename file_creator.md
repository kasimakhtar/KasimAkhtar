## Bash script to create new batch of files in folder

This bash script is designed to automatically create 25 new files in a directory, with file names in ascending order. The script assumes that the directory contains files with the same filename but with ascending numbers i.e. filename1, filename2, filename3, etc. The script also assumes the directory is being used to contain only these set of files and would not run properly if there was an anomolous file in the directory.

~~~

#! /bin/bash

#Find current total number of files in directory
FILE_NUM=$(cd /root/directory/ && ls | wc -l)

#Create variable to establish first file to be created
FIRST_ADD="1"

#Calculate the number for the filename of the first new file
FIRST_NEW_NUM=$(expr $FILE_NUM + $FIRST_ADD)

#Create variable for range of files to be created
SEC_ADD="25"

#Create range of new files to be created
TOTAL_NEW_NUM=$(expr $FILE_NUM + $SEC_ADD)

#Create new batch of 25 files 
for ((i=$FIRST_NEW_NUM;i<=$TOTAL_NEW_NUM;i++))
do
  touch /root/directory/filename${i}
done

