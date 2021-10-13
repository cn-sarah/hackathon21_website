# Dependencies

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Flask App
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G') 
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/maps', methods=['GET', 'POST'])
@app.route('/maps.html', methods=['GET', 'POST'])
def maps():
    return render_template('maps.html')

@app.route('/explore', methods=['GET', 'POST'])
@app.route('/explore.html', methods=['GET', 'POST'])
def explore():
    return render_template('explore.html')

@app.route('/donate', methods=['GET', 'POST'])
@app.route('/donate.html', methods=['GET', 'POST'])
def donate():
    return render_template('donate.html')

@app.route('/details', methods=['GET', 'POST'])
@app.route('/details.html', methods=['GET', 'POST'])
def details():
    return render_template('campaign-details.html')

@app.route('/campaigns', methods=['GET', 'POST'])
@app.route('/campaigns.html', methods=['GET', 'POST'])
@app.route('/campaign-details.html', methods=['GET', 'POST'])
def campaigns():
    return render_template('campaigns.html')

if __name__ == '__main__':
    # add ssl certificate
    app.run(ssl_context='adhoc')
