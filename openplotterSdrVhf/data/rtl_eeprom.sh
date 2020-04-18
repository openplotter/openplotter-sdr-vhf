#!/bin/bash

sdraisdeviceindex=$1
serial=$2
msg=$3

rtl_eeprom -d $sdraisdeviceindex -s $serial

echo "-----------------------------------------------------------------------"
echo $msg
echo "-----------------------------------------------------------------------"
read -p " "
