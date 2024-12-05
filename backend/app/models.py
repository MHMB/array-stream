from datetime import datetime
from . import mongo_client

class ArrayRecord:
    @staticmethod
    def save_array(array_data, size, range_start, range_end):
        db = mongo_client.array_generator
        return db.arrays.insert_one({
            'array': array_data.tolist(),
            'size': size,
            'range_start': range_start,
            'range_end': range_end,
            'created_at': datetime.utcnow()
        })
    
    @staticmethod
    def get_recent_arrays(limit=10):
        db = mongo_client.array_generator
        cursor = db.arrays.find().sort('created_at', -1).limit(limit)
        return list(cursor)