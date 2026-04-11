from flask import Flask, render_template, request
import requests

# FIXED: Vercel requires these to be at the absolute top level
app = Flask(__name__)
application = app

# --- AD CONFIGURATION ---
TOP_AD_CODE = '<div class="<script src="https://pl29119535.profitablecpmratenetwork.com/9a/21/2b/9a212becd0d90b0c9f7bbc2941c8a2fe.js"></script>
">✨ ADVERTISEMENT: CLICK TO UNLOCK PREMIUM FEATURES ✨</div>'
IN_FEED_AD = '<div class="<script src="https://pl29119535.profitablecpmratenetwork.com/9a/21/2b/9a212becd0d90b0c9f7bbc2941c8a2fe.js"></script>
">🎁 SPONSORED: EARN MONEY ONLINE - CLICK HERE 🎁</div>'

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
            .container {{ background-color: #1a1a1a; padding: 30px; border-radius: 12px; width: 90%; max-width: 400px; text-align: center; border: 1px solid #333; box-shadow: 0 8px 24px rgba(0,0,0,0.5); }}
            .ad-placeholder {{ background: #222; margin: 15px 0; padding: 15px; border: 1px dashed #4dabf7; color: #4dabf7; font-size: 14px; font-weight: bold; border-radius: 8px; cursor: pointer; }}
            input[type="text"] {{ width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #444; border-radius: 6px; background-color: #252525; color: white; box-sizing: border-box; font-size: 16px; }}
            button {{ width: 100%; padding: 12px; background-color: #228be6; border: none; border-radius: 6px; color: white; font-weight: bold; cursor: pointer; font-size: 16px; }}
            h2 {{ color: #4dabf7; margin-top: 0; }}
        </style>
    </head>
    <body>
        {TOP_AD_CODE}
        <div class="container">
            <h2>SIM Info Finder</h2>
            <form action="/search" method="post">
                <input type="text" name="track" placeholder="Enter Number or CNIC" required>
                <button type="submit">Search Database</button>
            </form>
        </div>
        {TOP_AD_CODE}
    </body>
    </html>
    '''

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('track')
    url = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
    payload = {"action": "fetch_simdata", "nonce": "e6a25f43de", "track": query}
    headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://simsownersdetails.com.pk/"}

    style = """
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #0f0f0f; color: #ffffff; padding: 20px; line-height: 1.6; }
        .result-container { max-width: 600px; margin: 0 auto; }
        .ad-placeholder { background: #1a1a1a; padding: 15px; margin: 20px 0; border: 2px solid #2ecc71; color: #2ecc71; text-align: center; font-weight: bold; border-radius: 10px; }
        .record-bar { background: #1a1a1a; padding: 20px; margin-bottom: 15px; border-radius: 10px; border-left: 6px solid #4dabf7; border-top: 1px solid #333; }
        .label { color: #4dabf7; font-weight: bold; font-size: 14px; text-transform: uppercase; }
        .value { font-size: 20px; font-weight: bold; color: #ffffff; display: block; margin-bottom: 5px; }
        .num-val { color: #2ecc71; font-size: 24px; }
        .back-btn { color: #4dabf7; text-decoration: none; font-weight: bold; font-size: 18px; }
    </style>
    """

    try:
        r = requests.post(url, data=payload, headers=headers)
        json_resp = r.json()
        output = f"{style}<div class='result-container'>{TOP_AD_CODE}<h1>Search Results</h1>"
        
        if json_resp.get("success"):
            data_content = json_resp.get("data", {})
            count = 0
            found_any = False
            
            for category, records in data_content.items():
                if isinstance(records, list):
                    for item in records:
                        found_any = True
                        if count % 2 == 0 and count != 0:
                            output += https://www.profitablecpmratenetwork.com/nc0hgef9nz?key=40fb6c3c7122759e8b07799f82d63383
                        
                        # Deep scan for number across all database keys
                        phone = item.get('Number') or item.get('id') or item.get('mobile') or item.get('phone') or "N/A"
                        
                        output += f'''
                        <div class="record-bar">
                            <span class="label">Number:</span> <span class="value num-val">{phone}</span>
                            <span class="label">Name:</span> <span class="value">{item.get('Name', 'N/A')}</span>
                            <span class="label">CNIC:</span> <span class="value">{item.get('CNIC', 'N/A')}</span>
                            <span class="label">Address:</span> <span class="value">{item.get('Address', 'N/A')}</span>
                            <small style="color:#555">Source: {category}</small>
                        </div>'''
                        count += 1

            if not found_any:
                return f"{style}<div class='result-container'><h2>No Records Found</h2><a href='/' class='back-btn'>← Back</a></div>"
            
            return output + f"{IN_FEED_AD}<br><a href='/' class='back-btn'>← Search Again</a></div>"
        
        return "<h3>Error fetching data.</h3>"
    except Exception as e:
        return f"<h3>System Error: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
