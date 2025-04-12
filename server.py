from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "https://happy-kitchen-backend.vercel.app"]}})
@app.route('/')
def home():
    return jsonify({
        "ingredients:": {
            "flour": "2 cups",
            "warm water": "3/4 cup",
            "sugar": "1 tsp",
            "salt": "1 tsp",
            "olive oil": "1 tbsp",
            "yeast": "1 tsp",
            "pizza sauce": "1/2 cup"
        },
        "instructions": [
            "In a bowl, mix warm water, sugar, and yeast. Let sit 5–10 minutes.",
            "Add flour, salt, and olive oil. Mix until dough forms.",
            "Knead on a floured surface for 5–8 minutes.",
            "Cover and let rise for 1–1.5 hours until doubled in size.",
            "Preheat oven to 475°F (245°C).",
            "Roll out the dough into a circle on parchment paper.",
            "Spread pizza sauce, add mozzarella, and top with basil.",
            "Bake for 10–13 minutes until the crust is golden and cheese is bubbly.",
            "Drizzle olive oil on top before serving."
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)