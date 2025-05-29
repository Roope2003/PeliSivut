import db
def add_items(Title,Description,Price,user_id ):
    sql = "INSERT INTO items (Title, Descriptio, Price, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [Title, Description, Price, user_id])
