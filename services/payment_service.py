import redis
import json
import time
from flask import Flask, jsonify

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# State variable to simulate a failure
IS_BROKEN = False

@app.route('/pay', methods=['GET'])
def process_payment():
    if IS_BROKEN:
        # Create the incident payload
        incident = {
            "service": "payment-service",
            "error_code": "DB_CONN_LIMIT",
            "details": "Database connection pool exhausted at 95% capacity",
            "timestamp": time.time()
        }
        # Publish to Redis
        r.publish('incidents', json.dumps(incident))
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500
    
    return jsonify({"status": "success", "message": "Payment Processed"}), 200

@app.route('/chaos/trigger', methods=['GET'])
def trigger_chaos():
    global IS_BROKEN
    IS_BROKEN = True
    return "Chaos Mode Enabled: Payment Service is now failing."

@app.route('/fix-pool', methods=['GET'])
def fix_pool():
    global IS_BROKEN
    IS_BROKEN = False
    return "Remediation Applied: Connection pool flushed and service restored."

if __name__ == "__main__":
    app.run(port=5001)