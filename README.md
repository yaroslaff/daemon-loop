# Daemon Loop
Daemon loop is simple and clean CLI utility to run programs periodically.

It's better alternative to running commands like:
~~~shell
while true; do date >> date.log; sleep 5; done 
~~~
(or even running such commands in screen/tmux sessions)

## Installation
~~~
pip3 install daemon-loop
~~~

## Usage
~~~
usage: loop [-h] [-n N] [-p PERIOD] [--log FILENAME] [-e] [-v] [-d]
            command [command ...]

Run command in loop (with features)

positional arguments:
  command               command with arguments

optional arguments:
  -h, --help            show this help message and exit
  -n N                  Run N times and exit (default: 0 = infinite)
  -p PERIOD, --period PERIOD
                        Run every N seconds (default: 60)
  --log FILENAME        Write command stdout to this file
  -e, --err             Write command stderr to logfile)
  -v, --verbose         Write loop technical info to logfile)
  -d, --daemon          Work as daemon
~~~

## Example usage
Simple and almost useless - run `date` every second until Ctrl-C:
~~~shell
$ loop date
Sun Dec 20 05:18:21 +07 2020
Sun Dec 20 05:19:21 +07 2020
Sun Dec 20 05:20:21 +07 2020
^C
~~~

Run `date +%s` (print unixtime) 3 times every 10 seconds and quit
~~~shell
$ loop -p 10 -n 3 -- date +%s
1608416485
1608416495
1608416505
~~~

And now something more useful - make our `date` program a daemon!
~~~shell
$ loop -dvep 10 --log /tmp/loop.log -- date +%s
$ pidof -x loop
25934
~~~

- `-d`: run as daemon
- `-v`: include technical info about time of start/stop, status code and daemon pid 
- `-e` (`--err`): include stderr to logfile
- `-p` (`--period`): period is 10 seconds
- `--log`: logfile

log file will look like this:
~~~
# 2020-12-20 05:39:01 my pid: 25934 run: date +%s
1608417541
# 2020-12-20 05:39:01 finished with status 0

# 2020-12-20 05:39:11 my pid: 25934 run: date +%s
1608417551
# 2020-12-20 05:39:11 finished with status 0

~~~ 
