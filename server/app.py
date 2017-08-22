import os
import sys
from modules import create_app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
