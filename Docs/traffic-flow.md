\# Traffic Flow



\## Hybrid Connectivity Flow



1\. An on-premises host initiates communication with an AWS resource.

2\. Traffic is routed through the Site-to-Site VPN tunnel.

3\. The VPN Attachment sends traffic to the AWS Transit Gateway.

4\. Transit Gateway determines the destination VPC using route tables.

5\. Traffic reaches the target EC2 instance inside the selected VPC.

6\. AWS Network Firewall can inspect traffic according to security policies.

7\. CloudTrail and AWS Config record network-related activities and configuration changes.



\## DNS Resolution Flow



\### On-Premises to AWS



1\. An on-premises host requests a private AWS domain name.

2\. The request is forwarded to the Route 53 Resolver Inbound Endpoint.

3\. Route 53 resolves the record and returns the private IP address.



\### AWS to On-Premises



1\. An AWS resource requests an on-premises private domain name.

2\. The request is sent to the Route 53 Resolver Outbound Endpoint.

3\. The query is forwarded to the on-premises DNS server.

4\. The DNS response is returned to the AWS resource.



