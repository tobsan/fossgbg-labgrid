

from labgrid import Environment
from labgrid.driver import ShellDriver
from labgrid.strategy import ShellStrategy

env = Environment('milliways.yaml')
t = env.get_target('main')
strat = t.get_driver(ShellStrategy)

# power cycle the device
strat.transition("off")
strat.transition("shell")

# get_driver() automatically activates
sh = t.get_driver(ShellDriver)
# Run command in shell and print the output
stdout, stderr, returncode = sh.run("cat /proc/cpuinfo")
for line in stdout:
    print(line)

