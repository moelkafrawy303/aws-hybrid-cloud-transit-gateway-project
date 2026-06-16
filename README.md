\# Hybrid Cloud Connectivity with AWS Transit Gateway and Site-to-Site VPN



\## Project Overview



This project demonstrates a hybrid cloud architecture connecting an on-premises data center to AWS using AWS Transit Gateway and Site-to-Site VPN. The design follows a hub-and-spoke model and includes multiple VPCs, hybrid DNS resolution, centralized security inspection, and monitoring services.



\---



\## Architecture Diagram



!\[Architecture Diagram](architecture/architecture-diagram.png)



\---



\## Architecture Components



\### On-Premises Data Center

\- On-Prem Router

\- On-Prem DNS Server

\- Internal Servers

\- CIDR: 192.168.0.0/16



\### AWS Transit Gateway

Acts as the central hub connecting all VPCs and the VPN attachment.



\### Site-to-Site VPN

\- IKEv2 VPN Tunnel

\- BGP Dynamic Routing

\- Customer ASN: 65000

\- AWS ASN: 64512



\### VPCs



\#### Dev VPC

\- CIDR: 10.10.0.0/16



\#### Staging VPC

\- CIDR: 10.20.0.0/16



\#### Prod VPC

\- CIDR: 10.30.0.0/16



\### Route 53 Resolver

\- Inbound Resolver Endpoint

\- Outbound Resolver Endpoint

\- Hybrid DNS Resolution



\### AWS RAM

Used to share networking resources across AWS accounts.



\### AWS Network Firewall

Provides centralized inspection for:

\- Inter-VPC Traffic

\- Internet Egress Traffic

\- Hybrid Traffic



\### Monitoring \& Governance

\- AWS CloudTrail

\- AWS Config



\---



\## CIDR Plan



| Network | CIDR |

|----------|----------|

| On-Premises | 192.168.0.0/16 |

| Dev VPC | 10.10.0.0/16 |

| Staging VPC | 10.20.0.0/16 |

| Prod VPC | 10.30.0.0/16 |



\---



\## Traffic Flow



1\. On-premises users access AWS resources through Site-to-Site VPN.

2\. Traffic enters AWS through the VPN Attachment.

3\. AWS Transit Gateway routes traffic to the target VPC.

4\. Route 53 Resolver handles hybrid DNS resolution.

5\. AWS Network Firewall inspects traffic before reaching its destination.

6\. CloudTrail and Config track network activity and configuration changes.



\---



\## Direct Connect vs Site-to-Site VPN



| Feature | Site-to-Site VPN | Direct Connect |

|----------|----------|----------|

| Connectivity | Internet-Based | Dedicated Connection |

| Cost | Lower | Higher |

| Setup Time | Fast | Longer |

| Bandwidth | Limited | High |

| Reliability | Good | Very High |



VPN is suitable for most hybrid environments, while Direct Connect is recommended for high-bandwidth and low-latency workloads.



\---



\## Security Considerations



\- Network segmentation using multiple VPCs.

\- Centralized traffic inspection using AWS Network Firewall.

\- Audit logging with CloudTrail.

\- Configuration compliance monitoring with AWS Config.

\- Secure encrypted VPN tunnel using IKEv2.



\---



\## Learning Outcomes



\- Design multi-VPC architectures using Transit Gateway.

\- Configure Site-to-Site VPN with BGP.

\- Implement hybrid DNS using Route 53 Resolver.

\- Compare Direct Connect and VPN architectures.

\- Apply centralized network security controls.

\- Monitor and audit AWS network environments.



\---



\## Conclusion



This project demonstrates a scalable and secure hybrid cloud architecture using AWS networking services and follows AWS best practices for connectivity, security, monitoring, and governance.

