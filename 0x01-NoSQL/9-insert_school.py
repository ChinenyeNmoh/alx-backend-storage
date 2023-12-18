def insert_school(mongo_collection, **kwargs):
    """Insert a school document into the MongoDB collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
