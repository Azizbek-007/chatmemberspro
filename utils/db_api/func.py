from sqlite3 import Error
import sqlite3 
from ast import literal_eval

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
        if not data:
            insert_query = f"INSERT INTO users(user_id, username, full_name) VALUES ('{user_id}', '{user_name}', '{full_name}')"
            self.post_sql_query(insert_query)
    
    def group_register (self, group_id):
        query = f"SELECT * FROM groups WHERE group_id='{group_id}'"
        data = self.post_sql_query(query)
        if not data:
            insert_query = f"INSERT INTO groups(group_id) VALUES ('{group_id}')"
            self.post_sql_query(insert_query)

    def user_and_group_count(self):
        user_query = "SELECT count(*) FROM users"
        u_count = self.post_sql_query(user_query)
        group = "SELECT count(*) FROM groups"
        g_count = self.post_sql_query(group)
        return u_count[0][0], g_count[0][0]
    
    def join_in_group (self, user_id, add_user_id, group_id):
        query = f"SELECT * FROM group_join WHERE user_id='{user_id}' AND group_id='{group_id}'"
        data = self.post_sql_query(query)
        if data == []: 
            added_users = []
            insert_query = f"INSERT INTO group_join(user_id, add_user_id, group_id) VALUES ('{user_id}', '{added_users}', '{group_id}')"
            self.post_sql_query(insert_query)
        else: 
            if len(data[0][2]) > 0:
                added_users = literal_eval(data[0][2]) 
            else: added_users = []
        if add_user_id not in added_users:
            added_users.append(add_user_id)
            insert_query = f"UPDATE group_join set add_user_id='{added_users}' where user_id='{user_id}' and group_id='{group_id}'"
            self.post_sql_query(insert_query)

    def my_members(self, user_id, group_id):
        query = f"SELECT add_user_id FROM group_join WHERE user_id='{user_id}' and group_id='{group_id}'"
        print(query)
        data = self.post_sql_query(query)
        if len(data) == 0: return 0
        return len(literal_eval(data[0][0]))
    
    def top_users (self, group_id):
        query = f"SELECT user_id, group_id, json_array_length(add_user_id) as _count FROM group_join WHERE group_id='{group_id}' ORDER BY _count DESC LIMIT 50"
        data = self.post_sql_query(query)
        return data
        
    
    def user_list(self):
        query = "SELECT * FROM users"
        return self.post_sql_query(query)
    
    def group_list(self):
        query = "SELECT * FROM groups"
        return self.post_sql_query(query)
    
    def group_list_limited(self, form):
        query = f"SELECT * FROM groups where id>{form}" 
        return self.post_sql_query(query)
    
    def group_list_limited_back(self, form):
        query = f"SELECT * FROM groups where id<{form} order by id desc" 
        return self.post_sql_query(query)
    
    def group_insert_channel(self, channel_id, group_id):
        query = f"UPDATE groups set channel_id='{channel_id}' where group_id='{group_id}'"
        self.post_sql_query(query)
        return True
    
    def group_set_status(self, group_id):
        query = f"UPDATE groups set status=0 where group_id='{group_id}'"
        self.post_sql_query(query)
        return True
    
    def user_set_status(self, user_id):
        query = f"UPDATE users set status=0 where user_id='{user_id}'"
        self.post_sql_query(query)
        return True
    
    def group_unset_channel(self, group_id):
        query = f"UPDATE groups set channel_id=NULL where group_id={group_id}"
        self.post_sql_query(query)

    def set_group_premissions(self, group_id, premissions):
        query = f"UPDATE groups set premissons='{premissions}' where group_id={group_id}"
        self.post_sql_query(query)
    
    def get_group_premissions(self, group_id):
        query = f"SELECT premissons FROM groups where group_id={group_id}"
        return self.post_sql_query(query)[0][0]


    def get_channel_id(self, group_id):
        query = f"SELECT channel_id FROM groups WHERE group_id='{group_id}'"
        channel_id = self.post_sql_query(query)[0][0]
        if channel_id != None:
            return channel_id
        else: return False

    def get_member_count(self, group_id):
        query = f"SELECT member_count FROM groups WHERE group_id='{group_id}'"
        member_count = self.post_sql_query(query)[0][0]
        if member_count != None:
            return member_count
        else: return False

    def get_chan(self, group_id):
        query = f"SELECT chan FROM groups WHERE group_id='{group_id}'"
        member_count = self.post_sql_query(query)[0][0]
        if member_count != None:
            return member_count
        else: return False

    def get_ads(self, group_id):
        query = f"SELECT ads FROM groups WHERE group_id='{group_id}'"
        member_count = self.post_sql_query(query)[0][0]
        if member_count != None:
            return member_count
        else: return False

    
    def add_member_count(self, group_id, _count):
        query = f"UPDATE groups set member_count='{_count}' where group_id={group_id}"
        self.post_sql_query(query)
    
    def unlimit(self, group_id):
        query = f"UPDATE groups set member_count=NULL WHERE group_id='{group_id}'"
        self.post_sql_query(query)

    def offads(self, group_id):
        query = f"UPDATE groups set ads=1 WHERE group_id='{group_id}'"
        self.post_sql_query(query)
    

    def onads(self, group_id):
        query = f"UPDATE groups set ads=NULL WHERE group_id='{group_id}'"
        self.post_sql_query(query)

    def offchan(self, group_id):
        query = f"UPDATE groups set chan=1 WHERE group_id='{group_id}'"
        self.post_sql_query(query)
    
    def onchan(self, group_id):
        query = f"UPDATE groups set chan=NULL WHERE group_id='{group_id}'"
        self.post_sql_query(query)

    def reset(self, group_id):
        query = f"UPDATE groups set chan=NULL, ads=NULL, member_count=NULL WHERE group_id='{group_id}'"
        self.post_sql_query(query)
        
    def clear_all_user(self, user_id):
        query = f"DELETE FROM group_join WHERE user_id='{user_id}'"
        self.post_sql_query(query)
    
    def clear_all_group(self, group_id):
        query = f"DELETE FROM group_join WHERE group_id='{group_id}'"
        self.post_sql_query(query)


    
DBS.top_users(DBS, 1)