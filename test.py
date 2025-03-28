import requests
import json

BASE_URL = "http://127.0.0.1:8000"

prompts = [
    "Show me all orders made by user with ID 1.",
    "Give me the total quantity of products ordered.",
    "List all products ordered by user with ID 1.",
    "What orders did user 1 place between IDs 1 and 5?",
    "Show the name and price of all products."
]

def get_query_explanation(prompt):
    response = requests.post(f"{BASE_URL}/query", json={"query": prompt})
    if response.status_code == 200:
        print(f"Prompt: {prompt}\n")
        explanation = response.json()
        print(f"SQL Generated: {explanation['sql_query']}")
        return explanation['sql_query']
    else:
        print(f"Error explaining query: {prompt}\n")
        return None

def validate_sql(sql_query):
    response = requests.post(f"{BASE_URL}/validate-sql", json={"sql": sql_query})
    if response.status_code == 200:
        print(f"Results for SQL Query: {sql_query}\n")
        print(response.json())
    else:
        print(f"Error validating query: {sql_query}\n")

def test_queries():
    for prompt in prompts:
        sql_query = get_query_explanation(prompt)
        
        if sql_query:
            validate_sql(sql_query)
        print("...............................................................................")
        print("")
        print("")


if __name__ == "__main__":
    test_queries()
