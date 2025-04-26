from openai import OpenAI
from dotenv import load_dotenv
import os
import re
import sqlite3
import sys

load_dotenv()

# connect to OpenAI
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY not found.")
    sys.exit(1)

client = OpenAI(
    api_key=OPENAI_API_KEY
)


DB_SCHEMA='''
Table: employees
- id (INT)
- name (TEXT)
- department_id (INT)

Table: departments
- id (INT)
- name (TEXT)
'''

def get_input() -> str:
    '''simply returns user input from argument or command line input'''
    if len(sys.argv) > 1:
        return sys.argv[1]
    return input('DB Question: ')

def main() -> None:
    '''main'''

    question = get_input() # get question about database

    # ask llm the question
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": f"""
You are an expert SQL assistant. Use the following database schema:

{DB_SCHEMA}

Generate an SQL query that answers the following question (NOTE: any department names start with a capital letter):

{question}
SQL:
        """}
    ],
    temperature=0
    )

    # keep necessary info
    content = completion.choices[0].message.content
    match = re.search(r"```sql\n(.*?)```", content, re.DOTALL)

    # question did not pertain to db, or did not generate valid response
    if not match:
        print('\nQuestion did not provide an SQL query.')
        return

    # collect the generated sql query
    sql_code = match.group(1)
    print('\nGenerated SQL query:')
    print(sql_code)

    # connect to db
    con = sqlite3.connect('excompany.db')
    cur = con.cursor()

    try:
        
        # execute query
        query = sql_code.strip()
        cur.execute(query)
        results = cur.fetchall()
        
    except Exception as e:
        
        # bad query, or SQL/db error
        print(f"Error: {e}")
        return
    
    finally:
        
        # close db
        cur.close()
        con.close()
        

    # print the result of the query
    print('Result of SQL query:')
    for result in results:
        print(" ".join(str(item) for item in result))


if __name__ == '__main__':
    main()