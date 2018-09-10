#! /bin/bash
var1=$(head -c 50 /dev/urandom | grep -oh -e "[A-Z]" -e "[0-9]" | grep -m 1 -oh "[A-Z0-9]")
var2=$(head -c 50 /dev/urandom | grep -oh -e "[A-Z]" -e "[0-9]" | grep -m 1 -oh "[A-Z0-9]")
var3=$(head -c 50 /dev/urandom | grep -oh -e "[A-Z]" -e "[0-9]" | grep -m 1 -oh "[A-Z0-9]")
var=$(echo $var1$var2$var3)
#echo $var
cat $1 | sed s/"\b[A-Z]\{2\}[0-9]\b"/$var/g


