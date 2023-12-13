Script for regular log rotation. A "rotate" folder is created in the log directory, where the compressed logs will be stored. At the moment the function of sending the compressed log to the server is not implemented. 

Mandatory command line arguments: 
-path: Path to the log file
-max-size: The maximum log size at which the log will be archived (in megabytes).
-inerval: Log file check interval (in seconds)
--max-log: The maximum number of archived logs at which the oldest log file will be deleted and sent to the server (depending on your -server argument value).
-server: If the argument value is "1", the log file will be sent to the server (not yet implemented), otherwise the log file will be deleted.
----------------------------------------------------------
Example: python3 pyrotate.py -path /var/log/syslog -max-size 5000 -interval 86400 -server 1 -max-log 5
----------------------------------------------------------

Warning!
Do not touch the contents of the rotate folder, otherwise the program may go wrong!
