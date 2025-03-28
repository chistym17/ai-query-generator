# **AI-Powered SQL Query Generator & Validator**  

This FastAPI-based project generates SQL queries from natural language prompts using an LLM and validates them by executing them against a database.  



## **Setup & Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/chistym17/ai-query-generator.git
cd ai-query-generator
```

### **2. Create a Virtual Environment**
```sh
python -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate     # On Windows  
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```
### **4. Set Up Environment Variables**
Create a .env file in the root directory and add the following:
```sh
TOGETHER_API_KEY=your_together_ai_api_key  
DATABASE_URL=your_postgresql_database_url  
```

### **5. Run the Application**
```sh
uvicorn main:app --reload
```
The API will be available at: http://127.0.0.1:8000

### **6. How to Test**
You can test the full workflow using the test.py script which will connect with the render backend url (does not require the project setup):
```sh
python test.py
```

This script:
Sends a natural language prompt to /query/ to generate an SQL query.

Retrieves the SQL query and explanation.

Sends the SQL query to /validate-sql/ for validation.

Executes the SQL and prints the validation results.




