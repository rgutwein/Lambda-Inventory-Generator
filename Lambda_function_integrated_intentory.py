import boto3
import openpyxl

# Set the region and service client
region = 'YOUR_REGION_HERE'
client = boto3.client('eks', region_name=region)

def create_inventory_spreadsheet(event, context):
    # Set the name of the EKS cluster
    cluster_name = 'YOUR_CLUSTER_NAME_HERE'

    # Get the list of nodes in the EKS cluster
    nodes = client.list_nodes(clusterName=cluster_name)['nodegroupList']
    # Flatten the list of nodes into a single list
    nodes = [node for node_group in nodes for node in node_group['status']['nodes']]

    # Create a new workbook and add a sheet for the inventory data
    workbook = openpyxl.Workbook()
    sheet = workbook.create_sheet('Inventory')

    # Add a header row to the sheet
    sheet.append(['Node Name', 'Instance Type', 'Instance ID', 'Instance Profile', 'IP Address', 'OS'])

    # Iterate through the nodes and add a row for each node
    for node in nodes:
        # Get the instance ID and instance profile ARN for the node
        instance_id = node['instanceId']
        instance_profile_arn = node['instanceProfileArn']

        # Get the instance information from the EC2 API
        instance = boto3.client('ec2', region_name=region).describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]

        # Extract the relevant instance information
        node_name = node['nodeName']
        instance_type = instance['InstanceType']
        instance_id = instance['InstanceId']
        instance_profile = instance_profile_arn.split('/')[-1]
        ip_address = instance['PrivateIpAddress']
        os = instance['Platform']

        # Add the instance information to the spreadsheet
        sheet.append([node_name, instance_type, instance_id, instance_profile, ip_address, os])

    # Save the workbook to a file
    workbook.save('inventory.xlsx')
