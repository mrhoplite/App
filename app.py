from flask import Flask, request
import requests

app = Flask(__name__)
application = app

# --- AD SLOTS ---
TOP_AD = '<div style="background:#222; margin:15px 0; padding:15px; border:1px dashed #4dabf7; color:#4dabf7; text-align:center; border-radius:8px; font-weight:bold;">✨ ADVERTISEMENT: CLICK TO UNLOCK PREMIUM FEATURES ✨</div>'

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SIM Finder</title>
        <style>
            body {{ font-family: sans-serif; background: #0f0f0f; color: #eee; padding: 20px; text-align: center; }}
            .box {{ background: #1a1a1a; padding: 20px; border-radius: 10px; border: 1px solid #333; max-width: 400px; margin: auto; }}
            input {{ width: 90%; padding: 10px; margin: 10px 0; background: #222; color: #fff; border: 1px solid #444; }}
            button {{ width: 95%; padding: 10px; background: #228be6; color: #fff; border: none; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        {TOP_AD}
        <div class="box">
            <h2 style="color:#4dabf7">SIM Database</h2>
            <form action="/search" method="post">
                <input type="text" name="track" placeholder="Enter CNIC or Number" required>
                <button type="submit">SEARCH NOW</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('track')
    url = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
    payload = {"action": "fetch_simdata", "nonce": "e6a25f43de", "track": query}
    headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://simsownersdetails.com.pk/"}

    try:
        r = requests.post(url, data=payload, headers=headers)
        json_resp = r.json()
        
        # Start the results page
        html = """<style>
            body { background: #0f0f0f; color: #fff; font-family: sans-serif; padding: 15px; }
            .card { background: #1a1a1a; border-left: 5px solid #2ecc71; padding: 15px; margin-bottom: 15px; border-radius: 5px; }
            .row { margin-bottom: 8px; border-bottom: 1px solid #333; padding-bottom: 4px; }
            .key { color: #4dabf7; font-weight: bold; font-size: 12px; text-transform: uppercase; }
            .val { font-size: 18px; display: block; }
        </style>"""
        
        html += f"{TOP_AD}<h1>Search Results</h1>"

        if json_resp.get("success"):
            data = json_resp.get("data", {})
            found = False

            # This loops through every category (Mobile, Server 2, Server Local, etc.)
            for category, records in data.items():
                if isinstance(records, list):
                    for item in records:
                        found = True
                        html += f'<div class="card"><div style="color:#666; font-size:10px;">Source: {category}</div>'
                        
                        # THE RAW DUMPER: This shows EVERY field the server sends back
                        for key, value in item.items():
                            if value: # Only show if the field isn't empty
                                html += f'<div class="row"><span class="key">{key}:</span> <span class="val">{value}</span></div>'
                        
                        html += "</div>"

            if not found:
                return "<h3>No data found for this query.</h3>"
            
            return html + "<br><a href='/' style='color:#4dabf7'>New Search</a>"
        
        return "<h3>Database Error. Please try again.</h3>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"
