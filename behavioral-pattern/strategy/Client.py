

from Traveler import Traveler
from Bus import Bus
from Taxi import Taxi
from Bicycle import Bicycle

a = Traveler(Bus())
a.go()

a = Traveler(Taxi())
a.go()

a = Traveler(Bicycle())
a.go()
