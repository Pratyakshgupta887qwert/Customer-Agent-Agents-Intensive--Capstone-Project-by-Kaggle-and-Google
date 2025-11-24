# api/index.py
def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": "<h2>Customer Intent Agent</h2><p>API is at <code>/api/predict</code></p>"
    }
