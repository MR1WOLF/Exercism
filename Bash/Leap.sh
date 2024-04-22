# Check if there's no args or if # of args > 1 or year is not integer number 
# Then Check if year is leap - If div by 4 then it's leap but if it's also div by 100
# it should be also div by 400 to be Leap Year, otherwise it's not a leap year.
year=$1
if [[ $# -ne 1 || $# -gt 1 ||  ! "$year" =~ ^[0-9]+$ ]]; then
    echo "Usage: leap.sh <year>";
    exit 1;
fi
if [[ $((year % 4)) -eq 0 ]]; then      
    if [[ $((year % 100)) -eq 0 ]]; then
        if [[ $((year % 400)) -eq 0 ]]; then
            is_leap="true"
        else
            is_leap="false"
        fi
    else
        is_leap="true"
    fi 
else
    is_leap="false"
fi

echo "$is_leap"
