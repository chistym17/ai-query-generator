from together import Together
from dotenv import load_dotenv
import os
from db.schema import DATABASE_SCHEMA  

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

class LLMQueryAgent:
    def __init__(self):
        self.client = Together(api_key=TOGETHER_API_KEY)

    def generate_query_and_explanation(self, user_query):
        """
        Generates both an SQL query and an explanation in a single call, using the predefined schema.
        """
        prompt = f"""
        You are an expert SQL assistant. Convert the following user request into an optimized SQL query 
        based on the given database schema and also provide a short explanation of how the SQL query works.

        DATABASE SCHEMA:
        {DATABASE_SCHEMA}

        User Query: "{user_query}"

        Respond in the following format:
        ```
        SQL Query:
        [Generated SQL Query]

        Explanation:
        [short explanation of how the SQL query was derived]
        ```
        """

        response = self.client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=700,
            temperature=0.5
        )

        response_text = response.choices[0].message.content.strip()

        sql_query = ""
        explanation = ""

        if "SQL Query:" in response_text and "Explanation:" in response_text:
            parts = response_text.split("Explanation:")
            sql_query = parts[0].replace("SQL Query:", "").strip()
            explanation = parts[1].strip()

        return sql_query, explanation
