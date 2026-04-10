from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# The secret keys we found in your screenshots
AJAX_URL = "https://simsownersdetails.com.pk/wp-admin/admin-ajax.php"
NONCE = "e6a25f43de" # Remember: update this if it expires!
ACTION = "fetch_simdata"

@app.route('/')
def index():
    # This renders the search bar page
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pro SIM Tracker</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; background: #121212; color: white; text-align: center; padding: 20px; }
            input { padding: 10px; border-radius: 5px; border: none; width: 80%; max-width: 300px; }
            button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
            .result-card { background: #1e1e1e; padding: 15px; margin-top: 20px; border-radius: 10px; border-left: 5px solid #007bff; text-align: left; display: inline-block; width: 90%; max-width: 400px; }
        </style>
    </head>
    <body>
        <h2>SIM Information Finder</h2>
        <form action="/search" method="post">
            <input type="text" name="query" placeholder="Enter Number or CNIC..." required>
            <button type="submit">Search</button>
        </form>
    </body>
    </html>
    '''

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form.get('query')
    
    payload = {
        "action": ACTION,
        "nonce": NONCE,
        "track": user_query # This was the 'key' found in your payload screenshot
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Android 13; Mobile; rv:125.0) Gecko/125.0 Firefox/125.0",
        "Referer": "https://simsownersdetails.com.pk/"
    }

    try:
        response = requests.post(AJAX_URL, data=payload, headers=headers)
        res_data = response.json()
        
        if res_data.get("success"):
            # Fetching the nested data we saw in your Network Response screenshot
            records = res_data.get("data", {}).get("Mobile", [])
            output = "<h1>Results Found:</h1>"
            for r in records:
                output += f'<div class="result-card"><b>Name:</b> {r.get("Name")}<br><b>CNIC:</b> {r.get("CNIC")}<br><b>Address:</b> {r.get("Address")}</div>'
            return output + '<br><br><a href="/" style="color:cyan;">Back to Search</a>'
        else:
            return "No records found or Nonce expired. <a href='/'>Try again</a>"
            
    except Exception as e:
        return f"Error connecting to database: {str(e)}"

if __name__ == '__main__':
