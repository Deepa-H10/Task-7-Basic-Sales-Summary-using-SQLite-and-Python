# Task 7: Basic Sales Summary using SQLite and Python

## Objective
Use SQL inside Python to pull sales info (like total quantity sold, total revenue) and visualize it.

## Tools Used
- Python (sqlite3, pandas, matplotlib)
- SQLite (built into Python, no setup required)

## Steps
1. Created a SQLite database `sales_data.db` with a `sales` table.
2. Inserted sample sales records (products, quantity, price).
3. Ran SQL queries inside Python using `sqlite3`.
4. Loaded results into pandas DataFrame.
5. Printed the sales summary.
6. Visualized revenue by product using matplotlib.

## Example Output

**Sales Summary:**

| Product     | Total Quantity | Revenue   |
|-------------|----------------|-----------|
| Laptop      | 8              | 474000    |
| Mobile      | 18             | 274000    |
| Tablet      | 10             | 206000    |
| Headphones  | 19             | 43500     |

**Bar Chart:**
Revenue by Product (saved as `sales_chart.png`)

## Interview Questions
- How did you connect Python to a database?
- What SQL query did you run?
- What does GROUP BY do?
- How did you calculate revenue?
- How did you visualize the result?
- What does pandas do in your code?
- What’s the benefit of using SQL inside Python?

---
✅ Submission ready!
