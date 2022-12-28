from sqlite3 import Error
import sqlite3 

class DBS:
    def post_sql_query(sql_query):
        with sqlite3.connect("./bot.db") as connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql_query)
                except Error:
                    pass
                result = cursor.fetchall()
                return result
        
    def create_users_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS USERS(           
            user_id TEXT,
            username TEXT,
            full_name TEXT)
        '''
        self.post_sql_query(query)
    
    def user_register (self, user_id, user_name, full_name):
        query = f"SELECT * FROM users WHERE user_id='{user_id}'"
        data = self.post_sql_query(query)
        print(data)
        if not data:
            insert_query = f"INSERT INTO users(user_id, username, full_name) VALUES ('{user_id}', '{user_name}', '{full_name}')"
            self.post_sql_query(insert_query)
    
    def group_register (self, group_id):
        query = f"SELECT * FROM groups WHERE group_id='{group_id}'"
        data = self.post_sql_query(query)
        print(data)
        if not data:
            insert_query = f"INSERT INTO groups(group_id) VALUES ('{group_id}')"
            self.post_sql_query(insert_query)

    def user_and_group_count(self):
        user_query = "SELECT count(*) FROM users"
        u_count = self.post_sql_query(user_query)
        group = "SELECT count(*) FROM groups"
        g_count = self.post_sql_query(group)
        return u_count[0][0], g_count[0][0]
    
    def join_in_group (self, user_id, add_user_id):
        query = f"SELECT * FROM group_join WHERE user_id='{user_id}' AND add_user_id='{add_user_id}'"
        data = self.post_sql_query(query)
        if not data:
            insert_query = f"INSERT INTO group_join(user_id, add_user_id) VALUES ('{user_id}', '{add_user_id}')"
            self.post_sql_query(insert_query)

    def my_members(self, user_id):
        query = f"SELECT count(*) FROM group_join WHERE user_id='{user_id}'"
        data = self.post_sql_query(query)
        return data[0]
    
    def top_users (self, group_id):
        query = f"SELECT user_id, group_id FROM group_join WHERE group_id='{group_id}'"
        data = self.post_sql_query(query)
        abc = []
        for x in data:
            query2 = f"SELECT count(user_id) FROM group_join WHERE user_id={x[0]}"
            data2 = self.post_sql_query(query2)
            if {x[0]: data2[0][0]} not in abc:
                abc.append({x[0]: data2[0][0]})
        


    
DBS.top_users(DBS, 1)