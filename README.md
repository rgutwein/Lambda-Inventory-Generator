# Lambda function to retrieve inventory information for an Amazon Elastic Container Service for Kubernetes (EKS) cluster and create an integrated inventory spreadsheet

This function gets the list of nodes in the specified EKS cluster using the ```list_nodes()``` method of the ```boto3``` library, which is the Amazon Web Services (AWS) SDK for Python. It then creates a new workbook using ```openpyxl``` and adds a sheet to the workbook for the inventory data. It adds a header row to the sheet and then iterates through the nodes, using the ```describe_instances()``` method of the ```boto3``` EC2 client to get the instance information for each node. It extracts the relevant information and adds it to the spreadsheet as a row. Finally, it saves the workbook to a file.

You will need to replace ```YOUR_REGION_HERE``` with the region where your EKS cluster is located and ```YOUR_CLUSTER_NAME_HERE``` with the name of your EKS cluster.
