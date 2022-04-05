from flask_restful import Resource

from ...models import Level


class questions(Resource):
    def get(self):

        # Fetch all game leves from database
        game_levels = Level.get_all()

        # Reeturn list of formatted levels to client
        return [level.assemble() for level in game_levels]
