from flask import Flask, request
import requests

app = Flask(__name__)
application = app

# --- AD CODES ---
POP_UNDER = '<script src="https://pl29119535.profitablecpmratenetwork.com/9a/21/2b/9a212becd0d90b0c9f7bbc2941c8a2fe.js"></script>'
SOCIAL_BAR = '<script src="https://pl29119538.profitablecpmratenetwork.com/b1/bf/65/b1bf65268b6a2f73410bd7768cf855ec.js"></script>'
SMART_LINK = "https://www.profitablecpmratenetwork.com/nc0hgef9nz?key=40fb6c3c7122759e8b07799f82d63383"

# SEO Metadata Block
SEO_META = '''
    <meta name="description" content="Check SIM Owner Details Pakistan 2026. Get fresh SIM information, CNIC data, and owner name/address from Server Local and Server 2 for Jazz, Zong, Telenor, and Ufone.">
    <meta name="keywords" content="sim owner details pakistan, pak sim data, sim information system, cnic info, check sim owner name, sim tracker, 668 sim check, fresh sim database 2026">
    <meta name="robots" content="index, follow">
'''

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SIM Owner Details Pakistan 2026 | Check SIM Info & CNIC Data</title>
        {SEO_META}
        {POP_UNDER}
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: #eee; padding: 20px; text-align: center; line-height: 1.6; }}
            .box {{ background: #1a1a1a; padding: 30px; border-radius: 12px; border: 1px solid #333; max-width: 450px; margin: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
            input {{ width: 90%; padding: 12px; margin: 15px 0; background: #252525; color: #fff; border: 1px solid #444; border-radius: 6px; font-size: 16px; }}
            button {{ width: 95%; padding: 12px; background: #228be6; color: #fff; border: none; font-weight: bold; cursor: pointer; border-radius: 6px; font-size: 16px; }}
            .premium-btn {{ display: block; margin-top: 15px; color: #fcc419; text-decoration: none; font-weight: bold; font-size: 14px; border: 1px solid #fcc419; padding: 10px; border-radius: 6px; }}
            .seo-section {{ max-width: 500px; margin: 40px auto; text-align: left; font-size: 14px; color: #888; border-top: 1px solid #333; padding-top: 20px; }}
            h2 {{ color: #4dabf7; font-size: 18px; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1 style="color:#4dabf7; font-size: 26px; margin-bottom:5px;">SIM Owner Details</h1>
            <p style="color:#666; font-size:12px; margin-top:0;">Official Pakistan SIM Information System</p>
            <form action="/search" method="post">
                <input type="text" name="track" placeholder="Enter Number (03XXXXXXXXX)" required>
                <button type="submit">SEARCH DATABASE</button>
            </form>
            <a href="{SMART_LINK}" target="_blank" class="premium-btn">✨ UNLOCK PREMIUM SERVER LOCAL ✨</a>
        </div>

        <div class="seo-section">
            <h2>How to Check Sim Owner Details Pakistan?</h2>
            <p>Welcome to <strong>Pak Sim Data</strong>, your trusted resource for <strong>Sim Owner Details Pakistan</strong>. Are you getting unknown calls? Use our tool to find <strong>SIM information</strong> and <strong>CNIC data</strong> instantly. We provide the latest <strong>Fresh SIM Database 2026</strong> for all networks including Jazz, Zong, Telenor, and Ufone.</p>
            
            <h3>Benefits of SIM Information System:</h3>
            <ul>
                <li>Identify unknown callers and spam numbers.</li>
                <li>Verify the number of SIMs registered on your CNIC.</li>
                <li>Access <strong>Server 2</strong> and <strong>Server Local</strong> records.</li>
            </ul>
        </div>

        {SOCIAL_BAR}
    </body>
    </html>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('track')
    url = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
    # Ensure this nonce is fresh!
    payload = {{"action": "fetch_simdata", "nonce": "cc094ee97c", "track": query}}
    headers = {{"User-Agent": "Mozilla/5.0", "Referer": "https://simsownersdetails.com.pk/"}}

    try:
        r = requests.post(url, data=payload, headers=headers)
        json_resp = r.json()
        
        html = f"""
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Results for {query} - SIM Owner Details</title>
            {SEO_META}
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
            <h2 style="color:#4dabf7">SIM Owner Results: {query}</h2>
        """

        if json_resp.get("success"):
            data = json_resp.get("data", {{}})
            found = False
            count = 0

            for category, records in data.items():
                if isinstance(records, list):
                    for item in records:
                        found = True
                        count += 1
                        html += f'<div class="card"><div style="color:#666; font-size:10px;">DATA SOURCE: {category}</div>'
                        for key, value in item.items():
                            if value:
                                html += f'<div class="row"><span class="key">{{key}}:</span> <span class="val">{{value}}</span></div>'
                        html += "</div>"
                        
                        if count == 3:
                            html += f'<a href="{SMART_LINK}" target="_blank" class="smart-box">🚀 SPEED UP SERVER CONNECTION 🚀</a>'

            if not found:
                return f"<h3>No data found for {{query}}.</h3><a href='{{SMART_LINK}}' style='color:yellow'>Try Premium Database Link</a>"
            
            html += f"<center>{SOCIAL_BAR}</center>"
            html += "<br><a href='/' style='color:#4dabf7; font-weight:bold;'>← New Search</a></body>"
            return html
        
        return "<h3>Database Error. Please refresh.</h3>"
    except Exception as e:
        return f"<h3>Error: {{str(e)}}</h3>"
