<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log Rotation Script</title>
</head>
<body>

<h1>Log Rotation Script</h1>

<p>This script automates log rotation by compressing log files based on size and rotating them at specified intervals. It also provides an option to send the compressed logs to a server.</p>

<h2>Usage</h2>

<pre><code>python3 pyrotate.py -path /var/log/syslog -max-size 5000 -interval 86400 -server 1 -max-log 5</code></pre>

<h3>Mandatory Command Line Arguments</h3>

<ul>
    <li><code>path</code>: Path to the log file.</li>
    <li><code>max-size</code>: The maximum log size at which the log will be archived (in megabytes).</li>
    <li><code>interval</code>: Log file check interval (in seconds).</li>
    <li><code>max-log</code>: The maximum number of archived logs at which the oldest log file will be deleted and sent to the server (depending on the <code>server</code> argument value).</li>
    <li><code>server</code>: If the argument value is "1", the log file will be sent to the server (not yet implemented), otherwise the log file will be deleted.</li>
</ul>

<h2>Important Note</h2>

<p>Do not touch the contents of the <code>rotate</code> folder, as it may disrupt the program's functionality.</p>

<h2>Features</h2>

<ul>
    <li><strong>Log Rotation</strong>: Automatically compresses logs based on the specified size.</li>
    <li><strong>Interval Rotation</strong>: Allows setting intervals for log file rotation.</li>
    <li><strong>Server Integration</strong>: Option to send logs to a server (not yet implemented).</li>
    <li><strong>Log Deletion</strong>: Deletes the oldest log files when the maximum log count is reached.</li>
</ul>

<h2>Contributing</h2>

<p>Feel free to contribute to the improvement of this log rotation script. Please create an issue or pull request for any enhancements or bug fixes.</p>

<h2>License</h2>

<p>This log rotation script is licensed under the <a href="LICENSE">MIT License</a>.</p>

</body>
</html>
