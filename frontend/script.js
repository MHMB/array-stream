const socket = io('http://localhost:5000');
const API_URL = 'http://localhost:5000/api';

// Socket.io event handlers
socket.on('connect', () => {
    console.log('Connected to WebSocket');
});

socket.on('new_array', (data) => {
    displayArray(data);
    loadArrayHistory();
});

// Functions to interact with the backend
async function generateArray() {
    const size = parseInt(document.getElementById('size').value);
    const rangeStart = parseInt(document.getElementById('range-start').value);
    const rangeEnd = parseInt(document.getElementById('range-end').value);

    socket.emit('generate_array', {
        size: size,
        range_start: rangeStart,
        range_end: rangeEnd
    });
}

async function loadArrayHistory() {
    try {
        const response = await fetch(`${API_URL}/history?limit=5`);
        const data = await response.json();
        
        const historyContainer = document.getElementById('array-history');
        historyContainer.innerHTML = data.map(item => `
            <div class="history-item">
                <p>Size: ${item.size}</p>
                <p>Range: ${item.range_start} - ${item.range_end}</p>
                <p>First 10 numbers: ${item.array.slice(0, 10).join(', ')}...</p>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading history:', error);
    }
}

function displayArray(data) {
    const arrayContainer = document.getElementById('current-array');
    arrayContainer.innerHTML = `
        <p>Generated array with size ${data.size}</p>
        <p>Range: ${data.range_start} - ${data.range_end}</p>
        <p>First 10 numbers: ${data.array.slice(0, 10).join(', ')}...</p>
    `;
}

// Load initial history
loadArrayHistory();
