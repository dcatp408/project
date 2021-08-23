from flask_app.models.monster import Monster
import flask_app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import app, flash

DATABASE = "card_game"


class Deck:
    def __init__(self, data):
        self.id = data["id"]
        self.created_at = data["created_at"]

    @classmethod
    def get_one(cls, id):
        query = "select * from deck where id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query)
        decks = []
        for decks in results:
            decks.append(cls(deck))
        return decks

    @classmethod
    def get_all_monsters_in_one_deck(cls, id):
        query = "select * from deck left join monster On deck.id = monster.deck_id where deck_id = %(deck_id)s"
        data = {
            "deck_id": id
        }
        results = connectToMySQL(DATABASE).query_db(query)
        decks = []
        for decks in results:
            decks.append(cls(deck))
        return decks
