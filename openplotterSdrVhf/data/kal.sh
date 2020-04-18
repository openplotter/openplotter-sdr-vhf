#!/bin/bash

sdraisdeviceindex=$1
task=$2
value=$3
ppm=$4
msg=$5

if [[ "$task" = "s" ]]; then
	kal -d $sdraisdeviceindex -s $value -e $ppm
else
	kal -d $sdraisdeviceindex -c $value -e $ppm
fi

echo "-----------------------------------------------------------------------"
echo $msg
echo "-----------------------------------------------------------------------"
read -p " "
