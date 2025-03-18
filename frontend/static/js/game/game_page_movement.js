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

let touchstartX = 0;
let touchstartY = 0;
let touchendX = 0;
let touchendY = 0;

function handleGesture() {
    let direction;
    if (touchendX < touchstartX) direction = 'left';
    if (touchendX > touchstartX) direction = 'right';
    if (touchendY < touchstartY) direction = 'up';
    if (touchendY > touchstartY) direction = 'down';
    if (direction) {
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
    }
}

document.addEventListener('touchstart', function(event) {
    touchstartX = event.changedTouches[0].screenX;
    touchstartY = event.changedTouches[0].screenY;
}, false);

document.addEventListener('touchend', function(event) {
    touchendX = event.changedTouches[0].screenX;
    touchendY = event.changedTouches[0].screenY;
    handleGesture();
}, false);