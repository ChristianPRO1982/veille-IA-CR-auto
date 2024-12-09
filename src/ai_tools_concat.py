import sqlite3
import os

def execute_query():
    file_path = 'output/tags.csv'
    open(file_path, 'w').close()

    conn = sqlite3.connect('output/ai_tools.db')
    cursor = conn.cursor()

    query = "DELETE FROM ai_tools_concat"
    cursor.execute(query)

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
    cursor.execute(query)

    query = """
SELECT CONCAT(id, ',', inner_url)
  FROM ai_tools_concat
 WHERE inner_url IS NOT NULL
"""
    cursor.execute(query)
    rows = cursor.fetchall()
    with open(file_path, 'a') as file:
        for row in rows:
            content = row[0]
            file.write(f'{content}\n')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    execute_query()