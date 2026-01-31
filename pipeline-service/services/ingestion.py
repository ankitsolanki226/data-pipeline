import requests
from sqlalchemy.orm import Session
from models.customer import Customer

FLASK_URL = "http://mock-server:5000/api/customers"

def ingest_customers(db: Session):
    page = 1
    limit = 10
    total_processed = 0

    while True:
        response = requests.get(FLASK_URL, params={"page": page, "limit": limit})
        data = response.json()
        customers = data["data"]

        if not customers:
            break

        for c in customers:
            existing = db.query(Customer).filter_by(customer_id=c["customer_id"]).first()

            if existing:
                for key, value in c.items():
                    setattr(existing, key, value)
            else:
                db.add(Customer(**c))

            total_processed += 1

        db.commit()
        page += 1

    return total_processed
