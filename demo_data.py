import sqlite3

# create a connection
conn = sqlite3.connect('demo_data.sqlite3')

# create a cursor
curs = conn.cursor()

# delete the table if this has already been ran
curs.execute('DROP TABLE IF EXISTS demo;')
conn.commit()

# create table to hold data
create_table_query = """
CREATE TABLE demo (
    s VARCHAR,
    x INT,
    y INT
);
"""

curs.execute(create_table_query)
conn.commit()

# create queries to insert data
insert_query_1 = """
INSERT INTO demo
VALUES ('g', 3, 9);
"""

curs.execute(insert_query_1)
conn.commit()

insert_query_2 = """
INSERT INTO demo
VALUES ('v', 5, 7);
"""

curs.execute(insert_query_2)
conn.commit()

insert_query_3 = """
INSERT INTO demo
VALUES ('f', 8, 7);
"""

curs.execute(insert_query_3)
conn.commit()

# check the demo database
row_count = """
SELECT COUNT(*) 
FROM demo;
"""

xy_at_least_5 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5 
AND y >= 5;
"""

unique_y = """
SELECT COUNT(DISTINCT y)
FROM demo;
"""
# print the results

print(curs.execute(row_count).fetchall()[0][0])
print(curs.execute(xy_at_least_5).fetchall()[0][0])
print(curs.execute(unique_y).fetchall()[0][0])

# close the connection
conn.close()