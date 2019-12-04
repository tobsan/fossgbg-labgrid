

from labgrid import Environment
from labgrid.protocol import ConsoleProtocol
from labgrid.strategy import ShellStrategy

env = Environment('milliways.yaml')
t = env.get_target('main')
strat = t.get_driver(ShellStrategy)

# power cycle the device
strat.transition("off")
strat.transition("shell")

# get_driver() automatically activates
cp = t.get_driver(ConsoleProtocol)
# Write to the console
cp.write(b'test')

