# http://trac.secdev.org/scapy/ticket/31 

# scapy3k.contrib.description = MPLS
# scapy3k.contrib.status = loads

from scapy3k.packet import Packet,bind_layers
from scapy3k.fields import BitField,ByteField
from scapy3k.layers.l2 import Ether

class MPLS(Packet): 
   name = "MPLS" 
   fields_desc =  [ BitField("label", 3, 20), 
                    BitField("cos", 0, 3), 
                    BitField("s", 1, 1), 
                    ByteField("ttl", 0)  ] 

bind_layers(Ether, MPLS, type=0x8847)
