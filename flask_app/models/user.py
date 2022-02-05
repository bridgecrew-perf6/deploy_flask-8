from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query  = "INSERT INTO users (first_name, email) VALUES (%(user_name)s,%(email)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id_AJAX(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return False
        return results[0]
    
    @classmethod
    def get_all_json(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        lst = [i for i in results]
        return lst