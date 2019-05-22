#!/bin/bash

# start gsm uart
sudo insmod /home/pi/git/uart_gsm/uart_gsm.ko
sleep 0.5

# start ardu uart
sudo insmod /home/pi/git/uart_ardu/uart_ardu.ko
sleep 0.5

#sudo insmod /home/pi/git/uart_gsm/uart_gsm.ko
#sleep 1
