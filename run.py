import os
from app import app

# Allow cross-origin requests from any domain
from flask_cors import CORS
CORS(app)

# Launch app
app.run(port=8000, debug=True)
