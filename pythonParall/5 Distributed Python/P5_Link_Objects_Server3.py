from __future__ import print_function
import Pyro5.api
import P5_Link_Objects_ChainTopology

this = "3"
next = "1"
servername = "example.chainTopology." + this

daemon = Pyro5.server.Daemon()
obj = P5_Link_Objects_ChainTopology.Chain(this, next)
uri = daemon.register(obj)

ns = Pyro5.api.locate_ns()
ns.register(servername, uri)

print("server_%s started " % this)
daemon.requestLoop()
