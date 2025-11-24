# api/index.py
def handler(request):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": "<!doctype html><html><head><meta charset='utf-8'><title>Customer Intent Agent</title></head>"
                "<body style='font-family:Arial,Helvetica,sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;'>"
                "<div style='text-align:center;'>"
                "<h1>Customer Intent Agent</h1>"
                "<p>API endpoint: <code>/api/predict</code></p>"
                "<p>Try a POST to <code>/api/predict</code> with JSON <code>{\"text\":\"I want to cancel\"}</code></p>"
                "</div></body></html>"
    }
