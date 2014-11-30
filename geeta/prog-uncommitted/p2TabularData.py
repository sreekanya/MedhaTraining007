from prettytable import PrettyTable
from prettytable import from_html
pts = from_html(html_string)
# db_cur is a Cursor object for your database
from prettytable import from_db_cursor
db_cur.execute("SELECT * FROM logindetails")
pt = from_db_cursor(db_cur)
