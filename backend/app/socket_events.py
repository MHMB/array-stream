import numpy as np
from . import socketio
from .models import ArrayRecord

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('generate_array')
def handle_generate_array(data):
    size = max(data.get('size', 10000), 10000)
    range_start = data.get('range_start', 0)
    range_end = max(data.get('range_end', 99999), 99999)
    
    array = np.random.randint(range_start, range_end + 1, size=size)
    
    # Save to MongoDB
    ArrayRecord.save_array(array, size, range_start, range_end)
    
    # Emit to all clients
    socketio.emit('new_array', {
        'array': array.tolist(),
        'size': size,
        'range_start': range_start,
        'range_end': range_end
    })