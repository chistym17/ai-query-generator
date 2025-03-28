import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User, Product, Order, Base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

user_names = [
    "Alice Smith", "Bob Johnson", "Charlie Brown", "David Williams", "Emma Davis",
    "Frank Miller", "Grace Wilson", "Hannah Moore", "Isaac Taylor", "Jack Anderson"
]

user_emails = [
    "alice.smith@example.com", "bob.johnson@example.com", "charlie.brown@example.com", 
    "david.williams@example.com", "emma.davis@example.com", "frank.miller@example.com", 
    "grace.wilson@example.com", "hannah.moore@example.com", "isaac.taylor@example.com", 
    "jack.anderson@example.com"
]

locations = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]

product_names = [
    "iPhone 13", "Samsung Galaxy S21", "Sony WH-1000XM4", "Dell XPS 13", "MacBook Pro",
    "Apple Watch Series 7", "Nikon D3500", "GoPro Hero 10", "Bose QuietComfort 35 II", "Kindle Paperwhite"
]

def generate_mock_data():
    users = [
        User(name=user_names[i], email=user_emails[i], age=random.randint(18, 65), location=locations[i])
        for i in range(10)
    ]

    products = [
        Product(name=product_names[i], price=random.uniform(50.0, 1500.0))
        for i in range(10)
    ]

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        session.add_all(users)
        session.add_all(products)

        session.commit()

        users = session.query(User).all()
        products = session.query(Product).all()

        orders = [
            Order(user_id=random.choice(users).id, product_id=random.choice(products).id, quantity=random.randint(1, 3))
            for _ in range(15)
        ]

        session.add_all(orders)

        session.commit()
        print("Mock data inserted successfully!")

if __name__ == "__main__":
    generate_mock_data()
