document.addEventListener('keydown', function(event) {
    let direction;
    switch(event.key) {
        case 'ArrowUp':
            direction = 'up';
            break;
        case 'ArrowDown':
            direction = 'down';
            break;
        case 'ArrowLeft':
            direction = 'left';
            break;
        case 'ArrowRight':
            direction = 'right';
            break;
        default:
            return;
    }
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ direction: direction })
    }).then(response => response.json()).then(data => {
        if (data.running === false) {
            document.getElementById('game-over').style.display = 'block';
        } else {
            location.reload();
        }
    });
});