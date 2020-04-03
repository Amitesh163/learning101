read a
read b
if [ $a -gt $b ]
then
    echo "X is greater than Y"
elif [ $a -lt $b ]
then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi
