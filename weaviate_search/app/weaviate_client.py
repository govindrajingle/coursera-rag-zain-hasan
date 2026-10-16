import weaviate

from config import WEAVIATE_URL


def get_client():
    return weaviate.connect_to_local(host="localhost", port=8080, grpc_port=50051)
