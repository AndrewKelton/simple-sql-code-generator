# Simple SQL Code Generator

**This program generates and runs sql queries for the _excompany_ database.** It takes a question about the database as input from the command line, and leverages OpenAI to generate an SQL query specifically for the schema specified below. It then runs the query on the example database to give the answer to the initial question.

## Requirements
* **Python3**
* **OpenAI API key**
* **`openai` & `sqlite3` libraries**

## Database Schema

### `employees`

| Column         | Type |
|----------------|------|
| `id`           | INT  |
| `name`         | TEXT |
| `department_id`| INT  |

### `departments`

| Column | Type |
|--------|------|
| `id`   | INT  |
| `name` | TEXT |