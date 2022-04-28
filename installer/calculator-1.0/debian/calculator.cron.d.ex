#
# Regular cron jobs for the calculator package
#
0 4	* * *	root	[ -x /usr/bin/calculator_maintenance ] && /usr/bin/calculator_maintenance
