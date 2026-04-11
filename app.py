from flask import Flask, render_template, request
import requests

# Standard Vercel entry point
app = Flask(__name__)
application = app

https://www.profitablecpmratenetwork.com/nc0hgef9nz?key=40fb6c3c7122759e8b07799f82d63383

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
            input[type="text"] { width: 100%; padding: 12px; margin-bottom: 20px; border: 1px solid #444; border-radius: 6px; background-color: #252525; color: white; box-sizing: border-box; font-size: 16px; }
            button { width: 100%; padding: 12px; background-color: #228be6; border: none; border-radius: 6px; color: white; font-weight: bold; cursor: pointer; transition: background 0.3s; font-size: 16px; }
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
    
    # Payload for the SIM database
    payload = {
        "action": "fetch_simdata",
        "nonce": "e6a25f43de",
        "track": query
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
        "Referer": "https://simsownersdetails.com.pk/"
    }

    # CSS to make results Large, White, and Professional
    style = """
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #0f0f0f; color: #ffffff; padding: 20px; font-size: 18px; line-height: 1.6; }
        .result-container { max-width: 700px; margin: 0 auto; }
        .result-title { color: #4dabf7; font-size: 32px; margin-bottom: 25px; font-weight: bold; border-bottom: 2px solid #333; padding-bottom: 10px; }
        .record-bar { 
            background: #1a1a1a; 
            padding: 25px; 
            margin-bottom: 20px; 
            border-radius: 12px; 
            border: 1px solid #444; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            border-left: 6px solid #2ecc71; /* Green side bar */
        }
        .label { color: #4dabf7; font-weight: bold; font-size: 16px; text-transform: uppercase; margin-right: 8px; }
        .value { font-size: 22px; font-weight: bold; color: #ffffff; }
        .number-value { color: #2ecc71; font-size: 24px; }
        .source-tag { font-size: 12px; color: #666; display: block; margin-top: 10px; text-align: right; }
        .back-link { color: #4dabf7; text-decoration: none; font-weight: bold; font-size: 20px; display: inline-block; margin-top: 20px; }
    </style>
    """

    try:
        r = requests.post(url, data=payload, headers=headers)
        json_resp = r.json()
        
        if json_resp.get("success"):
            data_content = json_resp.get("data", {})
            output = f"{style}<div class='result-container'><h1 class='result-title'>Database Results:</h1>"
            
            found_any = False

<script src="https://pl29119535.profitablecpmratenetwork.com/9a/21/2b/9a212becd0d90b0c9f7bbc2941c8a2fe.js"></script>

            
            # Loop through all server categories (Mobile, Server2, ServerLocal, etc.)
            for category in data_content:
                records = data_content[category]
                if isinstance(records, list):
                    for item in records:
                        found_any = True
                        output += '<div class="record-bar">'
                        
                        # Show Number if it exists
                        if item.get('Number'):
                            output += f'<div><span class="label">Number:</span> <span class="value number-value">{item.get("Number")}</span></div>'
                        
                        output += f'<div><span class="label">Name:</span> <span class="value">{item.get("Name")}</span></div>'
                        output += f'<div><span class="label">CNIC:</span> <span class="value">{item.get("CNIC")}</span></div>'
                        output += f'<div><span class="label">Address:</span> <span class="value">{item.get("Address")}</span></div>'
                        output += f'<span class="source-tag">Database Source: {category}</span>'
                        output += '</div>'

            if not found_any:
                return f"{style}<div class='result-container'><h2>No records found for this query.</h2><br><a href='/' class='back-link'>← Back to Search</a></div>"
            
            return output + "<a href='/' class='back-link'>← Search Again</a></div>"
        else:
            return f"{style}<div class='result-container'><h2>Error: Failed to fetch data.</h2><a href='/' class='back-link'>Back</a></div>"
    except Exception as e:
        return f"{style}<div class='result-container'><h2>System Error: {str(e)}</h2><a href='/' class='back-link'>Back</a></div>"
