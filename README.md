<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Log Rotation Script</h1>

<p>This script automates log rotation by compressing log files based on size and rotating them at specified intervals. It also provides an option to send the compressed logs to a server.</p>

[Docker Hub Repository](https://hub.docker.com/r/yareee/pyrotate)

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

<p>If you are using Docker, please take into account the following:</p>

<ol>
  <li>To grant the container access to logs, it should be launched with the additional argument <code>--mount type=bind,source=/var/log/syslog,target=/mnt/log</code>, where:</li>
  <ul>
    <li><code>source</code> is the path to the folder with logs on the host machine,</li>
    <li><code>target</code> is the path to the folder with logs visible within the container (it is not recommended to change the target). Ensure that the specified target folder exists in the file system hierarchy visible to the container. To create it, refer to point 3.</li>
  </ul>
  <li>The <code>-path</code> argument should be constructed according to the template <code>"target/log_file"</code>, where <code>target</code> is equal to the target specified in the <code>--mount</code> key.</li>
  <li>To create the necessary folder for the target value from point 1, run <code>docker build</code> with the <code>--build-arg logdir=/dir</code> argument, where <code>logdir</code> is the path to the new folder.</li>
</ol>

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

<p>This log rotation script is licensed under the <a href="https://github.com/ermantraun/pyrotate/blob/main/LICENSE">GNU License</a>.</p>

</body>
</html>
