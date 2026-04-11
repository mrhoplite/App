from flask import Flask, request
import requests

app = Flask(__name__)
application = app

# --- AD CONFIGURATION ---
TOP_AD = '<div style="background:#222; margin:15px 0; padding:15px; border:1px dashed #4dabf7; color:#4dabf7; text-align:center; border-radius:8px; font-weight:bold;">✨ ADVERTISEMENT: CLICK TO UNLOCK PREMIUM FEATURES ✨</div>'
FEED_AD = '<div style="background:#1a1a1a; padding:15px; margin:20px 0; border:2px solid #2ecc71; color:#2ecc71; text-align:center; border-radius:10px; font-weight:bold;">🎁 SPONSORED: EARN MONEY ONLINE - CLICK HERE 🎁</div>'

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SIM Details Finder</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background-color: #0f0f0f; color: #e0e0e0; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; flex-direction: column; }}
            .container {{ background-color: #1a1a1a; padding: 30px; border-radius: 12px; width: 90%; max-width: 400px; text-align: center; border: 1px solid #333; }}
            input[type="text"] {{ width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #444; border-radius: 6px; background-color: #252525; color: white; box-sizing: border-box; }}
            button {{ width: 100%; padding: 12px; background-color: #228be6; border: none; border-radius: 6px; color: white; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        {TOP_AD}
        <div class="container">
            <h2 style="color:#4dabf7;">SIM Info Finder</h2>
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://simsownersdetails.com.pk/"
    }

    style = """
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #0f0f0f; color: #ffffff; padding: 20px; }
        .res-container { max-width: 600px; margin: 0 auto; }
        .record-bar { background: #1a1a1a; padding: 20px; margin-bottom: 15px; border-radius: 10px; border-left: 6px solid #2ecc71; border: 1px solid #333; }
        .label { color: #4dabf7; font-weight: bold; font-size: 14px; text-transform: uppercase; }
        .value { font-size: 18px; font-weight: bold; color: #ffffff; display: block; margin-bottom: 5px; }
        .num-val { color: #2ecc71; font-size: 24px; margin-bottom: 10px; }
    </style>
    """

    try:
        r = requests.post(url, data=payload, headers=headers)
        json_resp = r.json()
        output = f"{style}<div class='res-container'>{TOP_AD}<h1>Search Results</h1>"
        
        if json_resp.get("success"):
            data_content = json_resp.get("data", {})
            count = 0
            found_any = False
            
            # This loop scans ALL servers (Server 2, Server Local, etc.)
            for category, records in data_content.items():
                if isinstance(records, list) and len(records) > 0:
                    for item in records:
                        found_any = True
                        if count % 2 == 0 and count != 0:
                            output += FEED_AD
                        
                        # CRITICAL FIX: The other sites use 'id' or 'Number' 
                        # This code now checks every possible field to find the digits
                        p = item.get('Number') or item.get('id') or item.get('phone') or item.get('mobile') or "Check Other Source"
                        
                        output += f'''
                        <div class="record-bar">
                            <span class="label">Number:</span> <span class="value num-val">{p}</span>
                            <span class="label">Name:</span> <span class="value">{item.get('Name', 'N/A')}</span>
                            <span class="label">CNIC:</span> <span class="value">{item.get('CNIC', 'N/A')}</span>
                            <span class="label">Address:</span> <span class="value">{item.get('Address', 'N/A')}</span>
                            <div style="font-size:10px; color:#666; text-align:right;">Database: {category}</div>
                        </div>'''
                        count += 1
            
            if not found_any:
                return f"{style}<h2>No data found.</h2><a href='/'>Back</a>"
            
            return output + f"<br><a href='/' style='color:#4dabf7;'>← Search Again</a></div>"
        return "<h3>Error: API rejected request.</h3>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
