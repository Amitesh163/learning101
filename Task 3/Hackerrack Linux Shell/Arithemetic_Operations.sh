read exp
printf "%.3f" $(echo "scale=4; $exp"|bc)
