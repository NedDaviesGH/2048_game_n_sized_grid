function startGame(size) {
    fetch('/start', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ size: size })
    }).then(response => response.json()).then(data => {
        if (data.success) {
            window.location.href = '/game';
        }
    });
}