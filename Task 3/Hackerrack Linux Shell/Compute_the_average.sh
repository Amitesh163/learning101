read n
sum=0
for ((i=0;i<$n;i++))
do
    read x
    sum=$(($sum+$x))
done
printf "%.3f" $(echo "scale=4; $sum/$n" | bc)
