DATABASE_SCHEMA = """
Tables:
1. Users
   - id (INT, PRIMARY KEY)
   - name (VARCHAR)
   - email (VARCHAR, UNIQUE)
   - age (INT)
   - location (VARCHAR)

2. Orders
   - id (INT, PRIMARY KEY)
   - user_id (INT, FOREIGN KEY references Users(id))
   - product_id (INT)
   - quantity (INT)

3. Products
   - id (INT, PRIMARY KEY)
   - name (VARCHAR)
   - price (DECIMAL)

Relationships:
- The `Orders` table links users and products.
- `user_id` in `Orders` is a foreign key referring to `Users(id)`.
- `product_id` in `Orders` is a foreign key referring to `Products(id)`.
"""
