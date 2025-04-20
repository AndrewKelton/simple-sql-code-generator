from openai import OpenAI
import re
import sqlite3

# openai api key
KEY=""

# connect to OpenAI
client = OpenAI(
    api_key=KEY
)

# main
def main():

    question = input('DB Question: ') # db question

    # ask question
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": f"""
You are an expert SQL assistant. Use the following database schema:

Table: employees
- id (INT)
- name (TEXT)
- department_id (INT)

Table: departments
- id (INT)
- name (TEXT)

Generate an SQL query that answers the following question:

{question}
SQL:
        """}
    ],
    temperature=0
    )

    # keep necessary info
    content = completion.choices[0].message.content
    match = re.search(r"```sql\n(.*?)```", content, re.DOTALL)

    # question did not pertain to db
    if not match:
        print('\nQuestion did not provide an SQL query.')
        return

    sql_code = match.group(1)
    print('\nGenerated SQL query:')
    print(sql_code)

    # connect to db
    con = sqlite3.connect('excompany.db')
    cur = con.cursor()

    # execute query
    query = sql_code.strip()
    cur.execute(query)
    results = cur.fetchall()

    # print the result of the query
    print('Result of SQL query:')
    for result in results:
        print(result[0])

    # close db
    cur.close()
    con.close()

if __name__ == '__main__':
    main()