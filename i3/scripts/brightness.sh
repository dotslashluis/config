#!/bin/bash

BRIGHT='cat brightness.conf'

if [ "$1" = '+' ]; then
	NEWBRIGHT=$(echo "$BRIGHT + 0.05" | bc)
	if [ "$(echo "$NEWBRIGHT -gt 1.0" | bc)" -eq 1 ]; then
		NEWBRIGHT='1.0'
	fi
elif [ "$1" = '-' ]; then
	    NEWBRIGHT=$(echo "$BRIGHT - 0.05" | bc)
	        if [ "$(echo "$NEWBRIGHT -lt 0.0" | bc)" -eq 1 ]; then
			        NEWBRIGHT='0.0'
				    fi
fi
