import flask_app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import app, flash

DATABASE = "card_game"


class Monster:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.attack = data["attack"]
        self.health = data["health"]
        self.type = data["type"]
        self.image = data["image"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.deck_id = data["deck_id"]

    # @classmethod
    # def get_one(cls, id):
    #     query = "select * from monster where id = %(id)s;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     monsters = []
    #     print("*"*80)
    #     print(results)
    #     print("*"*80)
    #     for monsters in results:
    #         monsters.append(cls(monster))
    #     return monsters[0]

    @classmethod
    def attack(self, target):
        target.health -= self.attack

        return self

    @classmethod
    def place(self):
        pass

    @classmethod
    def get_by_id(cls, data):
        query = 'SELECT * FROM monster WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)

        return result
