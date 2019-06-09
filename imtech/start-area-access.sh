#!/bin/bash

# start gsm uart
sudo insmod /home/pi/git/uart_gsm/uart_gsm.ko
sleep 0.1

# start ardu uart
sudo insmod /home/pi/git/uart_ardu/uart_ardu.ko
sleep 0.1

#sudo insmod /home/pi/git/uart_gsm/uart_gsm.ko
#sleep 1

# create data files
/home/pi/imtech/access-ctrl/create-db-files.py
sleep 0.1
echo "create-db-files"

# start send new keys script -> background
/home/pi/imtech/access-ctrl/send-new-keys.py &
sleep 0.1
echo "send-new-keys"

# start main ardu app -> background
/home/pi/imtech/access-ctrl/ardu-mon.py &
sleep 0.1
echo "ardu-mon"
