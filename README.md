# Simple SQL Code Generator

**This program generates and runs SQL queries for the _excompany.db_ database.**  
It takes a natural language question about the database—via `stdin` or as a command-line argument—and uses OpenAI's API to generate an SQL query based on the schema defined below.     
After receiving the generated SQL query, it then executes the query on the example database and prints the results of the original question.

## Requirements
* **Python3**
* **OpenAI API Key**
  see <a href="https://platform.openai.com">platform.openai</a>
* **`openai` Library**: ```pip install openai```

## Usage Example

```bash
$  python3 main.py "What are the ids and names of all employees in the sales and engineering department?"
```

```bash
 Generated SQL query:
 SELECT e.id, e.name
 FROM employees e
 JOIN departments d ON e.department_id = d.id
 WHERE d.name IN ('Sales', 'Engineering');
```

```bash
 Result of SQL query:
 1 Alice 
 2 Bob 
 3 Carol 
```

## Database Schema

<div style="display: flex; gap: 10px; font-size: 1.1em">

<div>

<b>employees</b>

<table>
  <tr><th>Column</th><th>Type</th></tr>
  <tr><td><code>id</code></td><td>INT</td></tr>
  <tr><td><code>name</code></td><td>TEXT</td></tr>
  <tr><td><code>department_id</code></td><td>INT</td></tr>
</table>
</div>

<div>

<b>departments</b>

<table>
  <tr><th>Column</th><th>Type</th></tr>
  <tr><td><code>id</code></td><td>INT</td></tr>
  <tr><td><code>name</code></td><td>TEXT</td></tr>
</table>
</div>

</div>

### Actual Sample Data

<div style="display: flex; gap: 10px; font-size: 1.1em">

<div>

<b>employees</b>

<table>
  <tr><th><code>id</code></th><th><code>name</code></th><th><code>department_id</code></th></tr>
  <tr><td>1</td><td>Alice</td><td>1</td></tr>
  <tr><td>2</td><td>Bob</td><td>2</td></tr>
  <tr><td>3</td><td>Carol</td><td>1</td></tr>
  <tr><td>4</td><td>Dave</td><td>3</td></tr>
</table>

</div>

<div>

<b>departments</b>

<table>
  <tr><th><code>id</code></th><th><code>name</code></th></tr>
  <tr><td>1</td><td>Sales</td></tr>
  <tr><td>2</td><td>Engineering</td></tr>
  <tr><td>3</td><td>HR</td></tr>
</table>

</div>

</div>