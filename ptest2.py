from flask import Flask, request
import subprocess

app = Flask(name)

@app.route("/dns")
def dns_lookup():
    hostname = request.values.get('hostname')
    cmd = 'nslookup ' + hostname
    output = subprocess.check_output(cmd, shell=True, text=True)
return output
if name == "main":
    app.run(debug=True)