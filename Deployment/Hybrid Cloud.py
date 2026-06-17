"""
Hybrid Cloud Connectivity Deployment Example

This script demonstrates how AWS networking resources
can be provisioned programmatically using Boto3.

Resources demonstrated:
- VPC
- Transit Gateway
- Transit Gateway Attachment

Note:
This script is for educational purposes and may require
additional parameters and permissions before execution.
"""

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")


def create_vpc(cidr_block: str, name: str):
    """Create a VPC and tag it."""
    try:
        response = ec2.create_vpc(
            CidrBlock=cidr_block
        )

        vpc_id = response["Vpc"]["VpcId"]

        ec2.create_tags(
            Resources=[vpc_id],
            Tags=[
                {"Key": "Name", "Value": name}
            ]
        )

        print(f"[+] Created VPC: {name} ({vpc_id})")
        return vpc_id

    except ClientError as error:
        print(f"[-] Failed to create VPC {name}: {error}")
        return None


def create_transit_gateway():
    """Create AWS Transit Gateway."""
    try:
        response = ec2.create_transit_gateway(
            Description="Hybrid Cloud Transit Gateway",
            Options={
                "AmazonSideAsn": 64512
            }
        )

        tgw_id = response["TransitGateway"]["TransitGatewayId"]

        print(f"[+] Created Transit Gateway: {tgw_id}")
        return tgw_id

    except ClientError as error:
        print(f"[-] Failed to create Transit Gateway: {error}")
        return None


def attach_vpc_to_tgw(transit_gateway_id, vpc_id, subnet_ids):
    """Attach a VPC to Transit Gateway."""
    try:
        response = ec2.create_transit_gateway_vpc_attachment(
            TransitGatewayId=transit_gateway_id,
            VpcId=vpc_id,
            SubnetIds=subnet_ids
        )

        attachment_id = response[
            "TransitGatewayVpcAttachment"
        ]["TransitGatewayAttachmentId"]

        print(f"[+] Created Attachment: {attachment_id}")
        return attachment_id

    except ClientError as error:
        print(f"[-] Failed to create attachment: {error}")
        return None


def main():
    print("Hybrid Cloud Connectivity Deployment Example")

    dev_vpc = create_vpc(
        cidr_block="10.10.0.0/16",
        name="Dev-VPC"
    )

    staging_vpc = create_vpc(
        cidr_block="10.20.0.0/16",
        name="Staging-VPC"
    )

    prod_vpc = create_vpc(
        cidr_block="10.30.0.0/16",
        name="Prod-VPC"
    )

    transit_gateway = create_transit_gateway()

    print("\nDeployment example completed.")
    print("Additional resources such as VPN,")
    print("Route 53 Resolver, Network Firewall,")
    print("CloudTrail, and AWS Config can be")
    print("added in future implementations.")


if __name__ == "__main__":
    main()