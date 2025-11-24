# api/predict.py
import json
import os
from app import Coordinator

# instantiate once per cold start (warm invocations reuse this)
agent = Coordinator()

def handler(request):
    """
    Vercel Python serverless function handler.
    Expects JSON body: {"text": "some message"}
    """
    try:
        # prefer request.json() if available
        data = request.json()
    except Exception:
        # fallback if request.json() not available
        body = b""
        if hasattr(request, "body"):
            try:
                # in some runtimes request.body is a stream
                body = request.body.read()
            except Exception:
                body = getattr(request, "body", b"")
        data = json.loads(body.decode() or "{}")

    text = data.get("text", "")
    out = agent.ask(text)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(out)
    }
