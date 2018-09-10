#! /bin/bash
cat $1 | sed 's/\b[A-Z]\{2\}[0-9]\b/***/g'
