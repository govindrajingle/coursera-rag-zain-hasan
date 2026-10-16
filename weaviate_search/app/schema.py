# for embdding via our model not default weaviate

import weaviate
from weaviate.classes.config import Configure, Property, DataType
from config import COLLECTION_NAME


def create_collection():
    client = weaviate.connect_to_local()
    try:
        # drop collection if it already exists
        if client.collections.exists(COLLECTION_NAME):
            print(f"deleted existing collection: {COLLECTION_NAME}")
        client.collection.create(
            name=COLLECTION_NAME,
            vectorizer_config=Configure.Vectorizer.none(),
            properties=[
                Property(
                    name="district",
                    data_type=DataType.TEXT,
                ),
                Property(
                    name="state",
                    data_type=DataType.TEXT,
                ),
                Property(
                    name="text",
                    data_type=DataType.TEXT,
                ),
            ],
        )
        print(f"created collection: {COLLECTION_NAME}")
    finally:
        client.close()


create_collection()
