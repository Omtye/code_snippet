import boto3

def get_rds_values(value):
    rds_client = boto3.client("rds")

    # 모든 RDS 클러스터 정보 가져오기
    db_clusters = rds_client.describe_db_clusters()

    # 클러스터 설정 값 가져오기
    for cluster in db_clusters["DBClusters"]:
        cluster_id = cluster["DBClusterIdentifier"]
        print(cluster_id, ":", cluster[value])

get_rds_values("EnabledCloudwatchLogsExports")
