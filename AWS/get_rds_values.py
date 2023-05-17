import boto3

def get_rds_values(value):
    rds_client = boto3.client("rds")

    # get all cluster
    db_clusters = rds_client.describe_db_clusters()

    # get cluster values
    for cluster in db_clusters["DBClusters"]:
        cluster_id = cluster["DBClusterIdentifier"]
        print(cluster_id, ":", cluster[value])

get_rds_values("EnabledCloudwatchLogsExports")
