@echo off
if exist input.txt del input.txt
if exist output.txt del output.txt
if exist ans.out del ans.out
python gen.py -o input.txt 10000 --max 1000
python ..\lab1.py -i input.txt -o output.txt mergesort
python sort.py -i input.txt -o ans.out
fc output.txt ans.out
pause
if exist input.txt del input.txt
if exist output.txt del output.txt
if exist ans.out del ans.out