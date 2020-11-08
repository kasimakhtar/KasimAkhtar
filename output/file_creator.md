## Bash script to create new batch of files in folder

This bash script is designed to automatically create 25 new files in a directory, each labelled with a number in ascending order. The script assumes there is a pre-existing pattern of these files in the folder in the format of a fixed "filename" and an ascending "number" i.e. filename1, filename2, filename3, etc.

~~~

#! /bin/bash

#Find current total number of files in folder
FILE_NUM=$(cd /home/folder/ && ls filename* | wc -l)

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
          touch /home/folder/filename${i}
  done

~~~

This is an example folder showing 25 empty files.

![example](URL)


This is the same folder after the script has been executed.

![example](URL)