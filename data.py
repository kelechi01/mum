import sqlite3

con = sqlite3.connect('exam.db')
cu = con.cursor()


cu.execute("""
    inert
""")




con.commit()
con.close()



