from flask import Flask, render_template, request
import requests

# This variable MUST be named 'app' for Vercel to find it
app = Flask(__name__)

# Essential for Vercel to handle the routing
application = app

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SIM Details Finder</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f0f0f; color: #e0e0e0; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background-color: #1a1a1a; padding: 30px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.5); width: 100%; max-width: 400px; text-align: center; border: 1px solid #333; }
            h2 { color: #00ff00; margin-bottom: 20px; }
            input[type="text"] { width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #444; border-radius: 6px; background-color: #252525; color: white; box-sizing: border-box; }
            button { width: 100%; padding: 12px; background-color: #228be6; border: none; border-radius: 6px; color: white; font-weight: bold; cursor: pointer; transition: background 0.3s; }
            button:hover { background-color: #1c7ed6; }
            .result { margin-top: 25px; text-align: left; background: #252525; padding: 15px; border-radius: 8px; border-left: 4px solid #00ff00; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>SIM Info Finder</h2>
            <form action="/search" method="post">
                <input type="text" name="track" placeholder="Enter Number or CNIC" required>
                <button type="submit">Search Database</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('track')
    
    # Using the exact keys from your successful manual search
    url = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
    payload = {
        "action": "fetch_simdata",
        "nonce": "e6a25f43de",
        "track": query
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
        "Referer": "https://simsownersdetails.com.pk/"
    }

    try:
        r = requests.post(url, data=payload, headers=headers)
        data = r.json()
        
        if data.get("success"):
            records = data.get("data", {}).get("Mobile", [])
            if not records:
                return "<h3>No records found.</h3><a href='/'>Back</a>"
            
            output = "<h2>Results:</h2>"
            for item in records:
                output += f'''
                <div style="background:#252525; padding:10px; margin-bottom:10px; border-radius:5px;">
                    <b>Name:</b> {item.get('Name')}<br>
                    <b>CNIC:</b> {item.get('CNIC')}<br>
                    <b>Address:</b> {item.get('Address')}
                </div>'''
            return output + "<br><a href='/' style='color:#4dabf7;'>Search Again</a>"
        else:
            return "<h3>Error: Search failed or Nonce expired.</h3><a href='/'>Back</a>"
    except Exception as e:
        return f"<h3>Connection Error: {str(e)}</h3>"
