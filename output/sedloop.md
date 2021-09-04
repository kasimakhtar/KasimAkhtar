## Bash sed command in a for loop
&nbsp;
This bash script works with this [python file](https://kasimakhtar.github.io/kasimakhtar/fintech_python.html). In the python file, the name of the datafile is mentioned. This script assumes you have a directory with lots of different datfiles. Rather than manually changing the datafile name in the python file, this bash script automates the process of changing and executing the python file each time. The commands for this are contained in a 'loop' function, and the output is stored in the 'list' array. 

~~~

list=()

loop () {
  for f in /path/to/data/Finance/Futures/*; do
    cleanf="${f##*/}"
    safeClean=$(printf '%s\n' "$cleanf" | sed 's/[[\.*^$/]/\\&/g')
    sed -i "s+Futures/.*')+Futures/"$safeClean"')+g" ../strategies/ADX.py
    python3.8 ../strategies/ADX.py
  done
}

IFS=$'\n' read -r -d '' -a list < <( loop && printf '\0' )
echo ${list[@]}

~~~
&nbsp;
In the python file, the financial indictor being tested is the ADX, hence the 'ADX.py' mentioned in the sed command above. But what if we wanted to test multiple indicators on one datafile at the same time. The bash script below assumes there is a directory with multiple python filse, each for a different financial indicator. The script loops through the list of python files, and changes the file name in the above script (i.e. ADX.py) to the next python file in the list. It then executes the above script. By using these two bash scripts together, it significantly reduces human effort.

~~~

for f in /root/future/run4-may-june/strategies/*; do
  cleanf="${f##*/}"
  safeClean=$(printf '%s\n' "$cleanf" | sed 's/[[\.*^$/]/\\&/g')
  sed -i "s+../strategies/.*+../strategies/"$safeClean"+g" rawDataLoop.sh
  ./rawDataLoop.sh
done

~~~













