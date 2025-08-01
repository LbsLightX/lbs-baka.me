document.addEventListener('DOMContentLoaded', () => {

    // --- THEME SWITCHER LOGIC ---
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        const applyTheme = (theme) => {
            if (theme === 'light') {
                document.body.classList.add('light-mode');
            } else {
                document.body.classList.remove('light-mode');
            }
        };

        let currentTheme = localStorage.getItem('theme') || 'dark';
        applyTheme(currentTheme);

        themeToggle.addEventListener('click', () => {
            currentTheme = document.body.classList.contains('light-mode') ? 'dark' : 'light';
            localStorage.setItem('theme', currentTheme);
            applyTheme(currentTheme);
        });
    }

    // --- DRAWING CANVAS LOGIC ---
    const canvas = document.getElementById('drawing-canvas');
    if (canvas) {
        const clearButton = document.getElementById('clear-canvas');
        const downloadButton = document.getElementById('download-canvas');
        const ctx = canvas.getContext('2d');
        let isDrawing = false;
        let lastPos = { x: 0, y: 0 };

        const setCanvasSize = () => {
            const parent = canvas.parentElement;
            canvas.width = parent.clientWidth;
            canvas.height = parent.clientHeight;
        };

        const getCoords = (e) => {
            const rect = canvas.getBoundingClientRect();
            const touch = e.touches && e.touches[0];
            return {
                x: (touch || e).clientX - rect.left,
                y: (touch || e).clientY - rect.top
            };
        };

        const startDrawing = (e) => {
            isDrawing = true;
            lastPos = getCoords(e);
        };

        const draw = (e) => {
            if (!isDrawing) return;
            e.preventDefault();
            const currentPos = getCoords(e);
            ctx.beginPath();
            ctx.moveTo(lastPos.x, lastPos.y);
            ctx.lineTo(currentPos.x, currentPos.y);
            ctx.strokeStyle = document.body.classList.contains('light-mode') ? '#1c1917' : '#ffffff';
            ctx.lineWidth = 2;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
            ctx.stroke();
            lastPos = currentPos;
        };

        const stopDrawing = () => {
            isDrawing = false;
        };

        clearButton.addEventListener('click', () => ctx.clearRect(0, 0, canvas.width, canvas.height));
        
        downloadButton.addEventListener('click', () => {
            const link = document.createElement('a');
            link.download = 'drawing.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
        });

        setCanvasSize();
        window.addEventListener('resize', setCanvasSize);
        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mousemove', draw);
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mouseleave', stopDrawing);
        canvas.addEventListener('touchstart', startDrawing, { passive: false });
        canvas.addEventListener('touchmove', draw, { passive: false });
        canvas.addEventListener('touchend', stopDrawing);
    }
});
