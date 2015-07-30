# A very simple Flask Hello World app for you to get started with...

import env

from flask import Flask

from go_http.metrics import MetricsApiClient

app = Flask(__name__)

def attach_metrics(app):
    app.metrics_api = MetricsApiClient(env['WEEDRAM_VUMIGO_API_TOKEN'])

attach_metrics(app)

@app.route('/')
def hello_world():
    metrics = app.metrics_api.get_metric(
        '.*', start='-7d', interval='1d', nulls='omit')
    metrics_html = str(metrics)
    html = """<html>
<head>
    <title>Weedram: A dash from a flask.</title>
</head>
<body>
    <h1>Metrics</h1>
    %s
</body>
</html>
    """ % metrics_html
    return html
