python pyarray.py > hexout
awk '{print $7 $8 $9 $10 $11 $12 $13 $14}' hexout | xxd -r -p

