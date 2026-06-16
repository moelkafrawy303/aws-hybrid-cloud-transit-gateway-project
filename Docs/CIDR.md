\# CIDR Plan



The project uses a non-overlapping IP addressing scheme to ensure proper routing between the on-premises environment and AWS VPCs.



| Network                 | CIDR Block     |

| ----------------------- | -------------- |

| On-Premises Data Center | 192.168.0.0/16 |

| Dev VPC                 | 10.10.0.0/16   |

| Staging VPC             | 10.20.0.0/16   |

| Prod VPC                | 10.30.0.0/16   |



\## Design Considerations



\* Non-overlapping CIDR ranges simplify routing.

\* Each environment is isolated in its own VPC.

\* Transit Gateway acts as the central routing hub.

\* The design can be extended with additional VPCs if required.



