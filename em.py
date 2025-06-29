from flask import Flask, render_template_string
import threading
import webbrowser
import time

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lời Chúc Lung Linh 💖</title>
        <style>
            body {
                margin: 0;
                overflow: hidden;
                background: radial-gradient(ellipse at center, #0a0a0a 0%, #000000 100%);
                font-family: 'Segoe UI', sans-serif;
                perspective: 1000px;
                animation: glowBackground 6s ease-in-out infinite alternate;
            }

            @keyframes glowBackground {
                0% { background-color: #000000; }
                100% { background-color: #1a0a1a; }
            }

            .text3d {
                position: absolute;
                white-space: nowrap;
                font-size: 24px;
                font-weight: bold;
                color: white;
                text-shadow: 0 0 10px rgba(255,255,255,0.6);
                transform-style: preserve-3d;
                opacity: 0.8;
                animation: fall linear;
            }

            @keyframes fall {
                0% {
                    transform: translateY(-100px) translateZ(var(--z)) scale(1);
                    opacity: 0;
                }
                20% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(120vh) translateZ(var(--z)) scale(1);
                    opacity: 0;
                }
            }

            .star {
                position: absolute;
                width: 2px;
                height: 2px;
                background: white;
                border-radius: 50%;
                opacity: 0.3;
                animation: twinkle 2s infinite ease-in-out alternate;
            }

            @keyframes twinkle {
                0% { opacity: 0.1; transform: scale(1); }
                100% { opacity: 1; transform: scale(1.5); }
            }
        </style>
    </head>
    <body>
        <script>
            const messages = [
                "Anh yêu em nhiều 💖",
                "Cảm ơn vì đã đến 💌",
                "Ai lớp diu bặc bặc 😘",
                "Luôn bên nhau 🫶",
                "He he he he he 🤭",
                "Tình iu sô nhìu 💞",
                "Xa mà gần 🌌",
                "Thương như hôm qua 🕊️",
                "Mỗi dòng là nhớ 💭"
            ];

            const emojis = ["❤️", "💖", "💌", "🥰", "😘", "💞", "💫", "🫶", "🌸"];

            function createFallingText() {
                const el = document.createElement("div");
                el.className = "text3d";
                el.innerText = messages[Math.floor(Math.random() * messages.length)];

                const left = Math.random() * window.innerWidth;
                const z = Math.floor(Math.random() * 1000 - 500);
                const duration = Math.random() * 5 + 4;

                el.style.left = `${left}px`;
                el.style.setProperty('--z', `${z}px`);
                el.style.animationDuration = `${duration}s`;

                document.body.appendChild(el);
                setTimeout(() => el.remove(), duration * 1000);
            }

            function createFallingEmoji() {
                const el = document.createElement("div");
                el.className = "text3d";
                el.innerText = emojis[Math.floor(Math.random() * emojis.length)];

                const left = Math.random() * window.innerWidth;
                const z = Math.floor(Math.random() * 1000 - 500);
                const duration = Math.random() * 5 + 4;

                el.style.left = `${left}px`;
                el.style.setProperty('--z', `${z}px`);
                el.style.animationDuration = `${duration}s`;
                el.style.fontSize = `${16 + Math.random() * 16}px`;
                el.style.opacity = 0.7;

                document.body.appendChild(el);
                setTimeout(() => el.remove(), duration * 1000);
            }

            function createStars(count = 80) {
                for (let i = 0; i < count; i++) {
                    const star = document.createElement("div");
                    star.className = "star";
                    star.style.left = Math.random() * window.innerWidth + "px";
                    star.style.top = Math.random() * window.innerHeight + "px";
                    star.style.animationDuration = (Math.random() * 2 + 1) + "s";
                    document.body.appendChild(star);
                }
            }

            // Khởi tạo
            createStars();

            // Lặp tạo hiệu ứng
            setInterval(createFallingText, 300);
            setInterval(createFallingEmoji, 400);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

def open_browser():
    time.sleep(1)
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(host="0.0.0.0", port=5000)
