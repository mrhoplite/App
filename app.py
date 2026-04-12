from flask import Flask, request
import requests

app = Flask(__name__)
application = app

# --- AD CODES ---
POP_UNDER = '<script src="https://pl29119535.profitablecpmratenetwork.com/9a/21/2b/9a212becd0d90b0c9f7bbc2941c8a2fe.js"></script>'
SOCIAL_BAR = '<script src="https://pl29119538.profitablecpmratenetwork.com/b1/bf/65/b1bf65268b6a2f73410bd7768cf855ec.js"></script>'
SMART_LINK = "https://www.profitablecpmratenetwork.com/nc0hgef9nz?key=40fb6c3c7122759e8b07799f82d63383"
BANNER_AD = '''<div style="margin:10px auto;text-align:center;"><script>atOptions={'key':'a054caf9ca9cf7989f60ed80b387020d','format':'iframe','height':90,'width':728,'params':{}};</script><script src="https://www.highperformanceformat.com/a054caf9ca9cf7989f60ed80b387020d/invoke.js"></script></div>'''

CSS = '''<style>
    body { background-color: #000; color: #fff; font-family: sans-serif; padding: 15px; text-align: center; }
    .box { background: #1a1a1a; padding: 25px; border-radius: 12px; border: 1px solid #333; max-width: 450px; margin: auto; }
    input { width: 90%; padding: 12px; margin: 10px 0; background: #252525; color: #fff; border: 1px solid #444; border-radius: 6px; }
    button { width: 95%; padding: 12px; background: #228be6; color: #fff; border: none; font-weight: bold; border-radius: 6px; cursor: pointer; }
    .card { background: #1a1a1a; border-left: 5px solid #2ecc71; padding: 15px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #333; text-align: left; }
    .key { color: #4dabf7; font-weight: bold; font-size: 11px; text-transform: uppercase; }
    .val { font-size: 18px; display: block; color: #fff; }
    .smart-box { background: #111; padding: 15px; border: 1px dashed #fcc419; color: #fcc419; text-align: center; border-radius: 8px; margin-bottom: 15px; text-decoration: none; display: block; font-weight: bold; }
</style>'''

@app.route('/')
def index():
    return f'''<html><head><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>SIM Owner Details 2026</title>{CSS}{POP_UNDER}</head>
    <body>{BANNER_AD}<div class="box"><h1 style="color:#4dabf7">SIM Owner Details</h1><form action="/search" method="post"><input type="text" name="track" placeholder="Enter Number" required><button type="submit">SEARCH NOW</button></form>
    <a href="{SMART_LINK}" target="_blank" style="color:#fcc419;display:block;margin-top:15px;text-decoration:none;">✨ PREMIUM SERVER ACCESS ✨</a></div>{SOCIAL_BAR}</body></html>'''

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('track')
    url = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
    # Updated Nonce: 4a0df85888
    payload = {"action": "fetch_simdata", "nonce": "4a0df85888", "track": query}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://simsownersdetails.com.pk/",
        "X-Requested-With": "XMLHttpRequest"
    }

    try:
        r = requests.post(url, data=payload, headers=headers, timeout=10)
        
        if r.status_code != 200:
            return f'''{CSS}<body>{BANNER_AD}<h3>Server Maintenance</h3><p>Direct database connection is currently limited.</p><a href="{SMART_LINK}" class="smart-box">⚡ ACCESS CLOUD DATABASE (FAST) ⚡</a><a href="/" style="color:#4dabf7">← Try Again</a>{SOCIAL_BAR}</body>'''

        json_resp = r.json()
        html = f'<html><head><meta name="viewport" content="width=device-width,initial-scale=1.0">{CSS}{POP_UNDER}</head><body>{BANNER_AD}'
        
        if json_resp.get("success"):
            data = json_resp.get("data", {})
            found = False
            for cat, records in data.items():
                if isinstance(records, list):
                    for item in records:
                        found = True
                        html += f'<div class="card">'
                        for k, v in item.items():
                            if v: html += f'<div><span class="key">{k}:</span> <span class="val">{v}</span></div>'
                        html += '</div>'
            
            if not found:
                html += f'<h3>No Data in Local Server</h3><a href="{SMART_LINK}" class="smart-box">CHECK GLOBAL DATABASE</a>'
        else:
            # If nonce is invalid, we guide them to the ad link
            html += f'<h3>Server Overloaded</h3><p>Please use our high-speed server below.</p><a href="{SMART_LINK}" class="smart-box">🚀 CONNECT TO PREMIUM SERVER 🚀</a>'

        html += f'<center>{SOCIAL_BAR}</center><br><a href="/" style="color:#4dabf7;font-weight:bold;text-decoration:none;">← Back</a>{BANNER_AD}</body></html>'
        return html

    except Exception:
        return f'''{CSS}<body>{BANNER_AD}<h3>Request Timeout</h3><a href="{SMART_LINK}" class="smart-box">TRY ALTERNATE SERVER</a><a href="/">← Back</a></body>'''
