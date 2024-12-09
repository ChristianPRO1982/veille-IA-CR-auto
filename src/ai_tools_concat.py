import sqlite3

def execute_query():
    # Connect to the SQLite database
    conn = sqlite3.connect('ai_tools.db')
    cursor = conn.cursor()

    # Define the SQL query
    query = """
INSERT INTO ai_tools_concat (category, title, description, type, inner_url, outer_url)
  SELECT GROUP_CONCAT(tmp.category, '||') AS category,
         tmp.title,
         GROUP_CONCAT(tmp.description, '||') AS description,
         GROUP_CONCAT(tmp.type, '||') AS type,
         GROUP_CONCAT(tmp.inner_url, '|') AS inner_url,
         tmp.outer_url
    FROM (
            SELECT GROUP_CONCAT(a.category, '||') AS category,
                   a.title,
                   a.description,
                   a.type,
                   a.inner_url,
                   a.outer_url
              FROM ai_tools a
          GROUP BY a.title, a.description, a.type, a.inner_url, a.outer_url
         ) as tmp
GROUP BY tmp.title, tmp.outer_url
    """

    # Execute the query
    cursor.execute(query)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    execute_query()