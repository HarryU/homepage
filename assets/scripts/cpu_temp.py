#!/usr/bin/python

import subprocess

cpuTemps = subprocess.check_output("/var/www/html/assets/scripts/cpu_temp.sh", shell=True)
print cpuTemps
result = dict()
for line in cpuTemps.split('\n'):
	if len(line) > 0:
		numberTemp = line.split(':')
		number = numberTemp[0].split('.')[2]
		temp = numberTemp[1].split('C')[0]
		with open('/var/www/html/assets/temps/' + str(number) + '.txt', 'w') as f:
			f.write(str(temp) + '&#176;C')

