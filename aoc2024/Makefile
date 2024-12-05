input:
	python3 new_day.py

%.in:
	curl -s 'https://adventofcode.com/2024/day/$(shell echo $* | sed s/^0//)/input' -H "Cookie: session=$$(cat cookie.txt)" > ./inputs/$@
