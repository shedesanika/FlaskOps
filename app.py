import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return f"""
    <html>
    <head>
        <title>Dynamic Flask Dashboard</title>

        <style>
            body {{
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                color: white;
                background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #00c9ff);
                background-size: 400% 400%;
                animation: gradientBG 12s ease infinite;
                transition: background 0.5s ease;
            }}

            .light-mode {{
                background: linear-gradient(135deg, #f6f9fc, #dfe9f3);
                color: #111;
            }}

            h1 {{
                margin-top: 30px;
                font-size: 42px;
                animation: fadeDown 1s ease;
            }}

            .clock {{
                font-size: 32px;
                color: #00f5d4;
                margin: 20px;
            }}

            .container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 20px;
            }}

            .card {{
                width: 550px;
                background: rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
                margin: 15px;
                padding: 20px;
                border-radius: 18px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.3);
                transition: transform 0.4s ease;
                animation: fadeUp 1s ease;
            }}

            .card:hover {{
                transform: scale(1.05);
            }}

            button {{
                padding: 12px 20px;
                border: none;
                border-radius: 10px;
                background: #00f5d4;
                cursor: pointer;
                font-size: 16px;
                margin: 20px;
            }}

            footer {{
                margin-top: 40px;
                padding: 20px;
                background: rgba(0,0,0,0.2);
            }}

            @keyframes gradientBG {{
                0% {{background-position: 0% 50%;}}
                50% {{background-position: 100% 50%;}}
                100% {{background-position: 0% 50%;}}
            }}

            @keyframes fadeDown {{
                from {{opacity:0; transform:translateY(-30px);}}
                to {{opacity:1; transform:translateY(0);}}
            }}

            @keyframes fadeUp {{
                from {{opacity:0; transform:translateY(30px);}}
                to {{opacity:1; transform:translateY(0);}}
            }}
        </style>
    </head>

    <body id="page">

        <h1>{greeting}, Welcome to FlaskOps</h1>

        <div class="clock" id="clock"></div>

        <button onclick="toggleTheme()">Toggle Theme</button>

        <div class="container">

            <div class="card">
                <h2>Server Status</h2>
                <p>Running Successfully</p>
            </div>

            <div class="card">
                <h2>Current Date</h2>
                <p>{now.strftime("%d %B %Y")}</p>
            </div>

            <div class="card">
                <h2>Environment</h2>
                <p>Dynamic Web Page</p>
            </div>

            <div class="card">
                <h2>Project</h2>
                <p>Interactive Flask Dashboard</p>
            </div>

        </div>

        <footer>
            Dynamic Dashboard • Created by <b>Sanika Shede</b>
        </footer>

        <script>
            function updateClock() {{
                const now = new Date();
                document.getElementById("clock").innerHTML =
                    now.toLocaleTimeString();
            }}

            setInterval(updateClock, 1000);
            updateClock();

            function toggleTheme() {{
                document.getElementById("page").classList.toggle("light-mode");
            }}
        </script>

    </body>
    </html>
    """

@app.route('/health')
def health():
    return {{"status": "healthy"}}

@app.route('/db-check')
def db_check():
    return "Dynamic page active"

if __name__ == '__main__':
    app.run(debug=True)