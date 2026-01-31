from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join("data", "customers.json")

def load_customers():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/api/customers", methods=["GET"])
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    customers = load_customers()
    total = len(customers)

    start = (page - 1) * limit
    end = start + limit
    paginated = customers[start:end]

    return jsonify({
        "data": paginated,
        "total": total,
        "page": page,
        "limit": limit
    })

@app.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customers = load_customers()
    for customer in customers:
        if customer["customer_id"] == customer_id:
            return jsonify(customer)
    return jsonify({"error": "Customer not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
