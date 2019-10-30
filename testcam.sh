raspivid -n -ih -t 60000 -w 1280 -h 720 -b 1000000 -fps 15 -o - | nc -lkv4 5001 
