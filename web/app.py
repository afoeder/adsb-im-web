from flask import Flask, redirect, render_template
app = Flask(__name__)

data = {
	"feeder_status": """We haven't seen an ADS-B image from your IP address connect to our server. If you have booted your single board computer with the ADSB.im image and still get this message, please take a look at the troubleshooting section in our <a href="/faq">FAQ</a>."""
}

@app.route('/')
def index():
	return redirect('/home', code=301)

@app.route('/<path:page>')
def page(page):
	return render_template(f'{page}.html', data=data)

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=8000)
