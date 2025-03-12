function sendCommand(action) {
    fetch(`/control/${action}`)
        .then(response => response.json())
        .then(data => alert(data.status))
        .catch(error => console.error('Error:', error));
}
