from flask import Flask, request
import requests

app = Flask(__name__)
application = app

# --- AD CODES ---
# Pop-under: High revenue, invisible until click
POP_UNDER = '<script src="https://pl29119535.profitablecpmratenetwork.com/9a/21/2b/9a212becd0d90b0c9f7bbc2941c8a2fe.js"></script>'

# Social Bar: WhatsApp/Notification style alerts
SOCIAL_BAR = '<script src="https://pl29119538.profitablecpmratenetwork.com/b1/bf/65/b1bf65268b6a2f73410bd7768cf855ec.js"></script>'

# Smart Link: Direct money link
SMART_LINK = "https://www.profitablecpmratenetwork.com/nc0hgef9nz?key=40fb6c3c7122759e8b07799f82d63383"

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SIM Finder</title>
        {POP_UNDER}
        <style>
            body {{ font-family: sans-serif; background: #0f0f0f; color: #eee; padding: 20px; text-align: center; }}
            .box {{ background: #1a1a1a; padding: 25px; border-radius: 12px; border: 1px solid #333; max-width: 400px; margin: auto; }}
            input {{ width: 90%; padding: 12px; margin: 15px 0; background: #222; color: #fff; border: 1px solid #444; border-radius: 6px; }}
            button {{ width: 95%; padding: 12px; background: #228be6; color: #fff; border: none; font-weight: bold; cursor: pointer; border-radius: 6px; }}
            .premium-btn {{ display: block; margin-top: 15px; color: #fcc419; text-decoration: none; font-weight: bold; font-size: 14px; border: 1px solid #fcc419; padding: 10px; border-radius: 6px; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2 style="color:#4dabf7">SIM Database</h2>
            <form action="/search" method="post">
                <input type="text" name="track" placeholder="Enter CNIC or Number" required>
                <button type="submit">SEARCH NOW</button>
            </form>
            <a href="{SMART_LINK}" target="_blank" class="premium-btn">✨ UNLOCK PREMIUM SERVER 2 ✨</a>
        </div>
        {SOCIAL_BAR}
    </body>
    </html>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('track')
    url = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
    payload = {"action": "fetch_simdata", "nonce": "cc094ee97c", "track": query}
    headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://simsownersdetails.com.pk/"}

    try:
        r = requests.post(url, data=payload, headers=headers)
        json_resp = r.json()
        
        html = f"""
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {POP_UNDER}
            <style>
                body {{ background: #0f0f0f; color: #fff; font-family: sans-serif; padding: 15px; }}
                .card {{ background: #1a1a1a; border-left: 5px solid #2ecc71; padding: 15px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #333; }}
                .row {{ margin-bottom: 8px; border-bottom: 1px solid #333; padding-bottom: 4px; }}
                .key {{ color: #4dabf7; font-weight: bold; font-size: 11px; text-transform: uppercase; }}
                .val {{ font-size: 18px; display: block; }}
                .smart-box {{ background: #222; padding: 15px; border: 1px dashed #fcc419; color: #fcc419; text-align: center; border-radius: 8px; margin-bottom: 15px; text-decoration: none; display: block; font-weight: bold; }}
            </style>
        </head>
        <body>
            <a href="{SMART_LINK}" target="_blank" class="smart-box">🎁 CLICK TO SEE HIDDEN NUMBERS (FREE) 🎁</a>
            <h1>Search Results</h1>
        """

        if json_resp.get("success"):
            data = json_resp.get("data", {})
            found = False
            count = 0

            for category, records in data.items():
                if isinstance(records, list):
                    for item in records:
                        found = True
                        count += 1
                        
                        # Show Social Bar script again after results
                        html += f'<div class="card"><div style="color:#666; font-size:10px;">Source: {category}</div>'
                        for key, value in item.items():
                            if value:
                                html += f'<div class="row"><span class="key">{key}:</span> <span class="val">{value}</span></div>'
                        html += "</div>"
                        
                        # Place a smart link in the middle of long results
                        if count == 3:
                            html += f'<a href="{SMART_LINK}" target="_blank" class="smart-box">🚀 SPEED UP SERVER CONNECTION 🚀</a>'

            if not found:
                return f"<h3>No data found.</h3><a href='{SMART_LINK}' style='color:yellow'>Try Premium Link</a>"
            
            html += f"<center>{SOCIAL_BAR}</center>"
            html += "<br><a href='/' style='color:#4dabf7; font-weight:bold;'>← New Search</a></body>"
            return html
        
        return "<h3>Database Error.</h3>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
