import time
import threading as t
from topf import *
from topo import *
from topi import *

i1 = t.Thread(target=ism)
f1 = t.Thread(target=familiya)
o1 = t.Thread(target=otchestvo)

i1.start()
f1.start()
o1.start()
