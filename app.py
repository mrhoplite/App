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
            h2 { color: #4dabf7; margin-bottom: 20px; }
            input[type="text"] { width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #444; border-radius: 6px; background-color: #252525; color: white; box-sizing: border-box; }
            button { width: 100%; padding: 12px; background-color: #228be6; border: none; border-radius: 6px; color: white; font-weight: bold; cursor: pointer; transition: background 0.3s; }
            button:hover { background-color: #1c7ed6; }
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

    # CSS to make results large, white, and visible
    style = """
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #0f0f0f; color: #ffffff; padding: 20px; font-size: 20px; }
        .result-title { color: #4dabf7; font-size: 30px; margin-bottom: 20px; font-weight: bold; }
        .record-bar { 
            background: #1a1a1a; 
            padding: 25px; 
            margin-bottom: 15px; 
            border-radius: 10px; 
            border: 1px solid #444; 
            color: #ffffff; 
            line-height: 1.8;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .label { color: #4dabf7; font-weight: bold; }
        .back-link { color: #4dabf7; text-decoration: none; font-size: 20px; font-weight: bold; display: inline-block; margin-top: 20px; }
    </style>
    """

    try:
        r = requests.post(url, data=payload, headers=headers)
        data = r.json()
        
        if data.get("success"):
            records = data.get("data", {}).get("Mobile", [])
            if not records:
                return f"{style}<h2 class='result-title'>No records found.</h2><a href='/' class='back-link'>← Back</a>"
            
            output = f"{style}<h2 class='result-title'>Results:</h2>"
            for item in records:
                output += f'''
                <div class="record-bar">
                    <span class="label">Name:</span> {item.get('Name')}<br>
                    <span class="label">CNIC:</span> {item.get('CNIC')}<br>
                    <span class="label">Address:</span> {item.get('Address')}
                </div>'''
            return output + "<br><a href='/' class='back-link'>← Search Again</a>"
        else:
            return f"{style}<h3 class='result-title'>Error: Search failed or Nonce expired.</h3><a href='/' class='back-link'>Back</a>"
    except Exception as e:
        return f"{style}<h3 class='result-title'>Connection Error: {str(e)}</h3>"
