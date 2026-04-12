from flask import Flask, request

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
    input { width: 90%; padding: 12px; margin: 10px 0; background: #252525; color: #fff; border: 1px solid #444; border-radius: 6px; font-size: 16px; }
    button { width: 95%; padding: 12px; background: #228be6; color: #fff; border: none; font-weight: bold; border-radius: 6px; cursor: pointer; }
    #results { margin-top: 20px; text-align: left; max-width: 450px; margin-left: auto; margin-right: auto; }
    .card { background: #1a1a1a; border-left: 5px solid #2ecc71; padding: 15px; margin-bottom: 15px; border: 1px solid #333; border-radius: 5px; }
    .key { color: #4dabf7; font-weight: bold; font-size: 11px; text-transform: uppercase; }
    .val { font-size: 18px; display: block; color: #fff; }
    .loading { color: #fcc419; font-weight: bold; }
</style>'''

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <title>SIM Data Finder 2026</title>
        {CSS}
        {POP_UNDER}
    </head>
    <body>
        {BANNER_AD}
        <div class="box">
            <h1 style="color:#4dabf7">SIM Owner Details</h1>
            <input type="text" id="number" placeholder="Enter Number (03XXXXXXXXX)">
            <button onclick="fetchData()">SEARCH NOW</button>
            <div id="status"></div>
        </div>
        
        <div id="results"></div>

        <script>
        async function fetchData() {{
            const num = document.getElementById('number').value;
            const resDiv = document.getElementById('results');
            const status = document.getElementById('status');
            
            if(!num) return alert("Enter number");
            
            resDiv.innerHTML = "";
            status.innerHTML = "<p class='loading'>Connecting to Secure Database...</p>";

            const formData = new FormData();
            formData.append('action', 'fetch_simdata');
            formData.append('nonce', '4a0df85888');
            formData.append('track', num);

            try {{
                const response = await fetch('https://simsownersdetails.net.pk/wp-admin/admin-ajaz.php', {{
                    method: 'POST',
                    body: formData
                }});

                const json = await response.json();
                status.innerHTML = "";

                if(json.success) {{
                    let html = "";
                    for (const [key, val] of Object.entries(json.data)) {{
                        val.forEach(item => {{
                            html += '<div class="card">';
                            for (const [k, v] of Object.entries(item)) {{
                                if(v) html += `<div><span class="key">${{k}}:</span><span class="val">${{v}}</span></div>`;
                            }}
                            html += '</div>';
                        }});
                    }}
                    resDiv.innerHTML = html || "<h3>No records found.</h3>";
                }} else {{
                    resDiv.innerHTML = "<h3>Security Error. Please try again.</h3>";
                }}
            }} catch (err) {{
                status.innerHTML = "";
                resDiv.innerHTML = `<h3>Server Blocked</h3><p>Direct access is limited. Use Premium Server:</p><a href="{SMART_LINK}" style="color:yellow;font-weight:bold;text-decoration:none;display:block;padding:15px;border:1px dashed yellow;">🎁 OPEN PREMIUM DATABASE 🎁</a>`;
            }}
        }}
        </script>
        {SOCIAL_BAR}
    </body>
    </html>
    '''
