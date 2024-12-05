from flask import Blueprint, jsonify, request
import numpy as np
from .models import ArrayRecord

api = Blueprint('api', __name__)

@api.route('/generate', methods=['POST'])
def generate_array():
    data = request.get_json()
    size = max(data.get('size', 10000), 10000)
    range_start = data.get('range_start', 0)
    range_end = max(data.get('range_end', 99999), 99999)
    
    array = np.random.randint(range_start, range_end + 1, size=size)
    
    # Save to MongoDB
    ArrayRecord.save_array(array, size, range_start, range_end)
    
    return jsonify({
        'array': array.tolist(),
        'size': size,
        'range_start': range_start,
        'range_end': range_end
    })

@api.route('/history', methods=['GET'])
def get_history():
    limit = int(request.args.get('limit', 10))
    arrays = ArrayRecord.get_recent_arrays(limit)
    
    # Convert ObjectId to string for JSON serialization
    for array in arrays:
        array['_id'] = str(array['_id'])
    
    return jsonify(arrays)