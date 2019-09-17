"""Run pedlarweb."""
import argparse
from pedlarweb import app, socketio

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-d", "--debug", action="store_true", help="Enable debug server.")
parser.add_argument("--host", default="127.0.0.1", help="Host IP address.")
parser.add_argument("--port", default=5000, type=int, help="Host port.")
ARGS = parser.parse_args()

if __name__ == "__main__":
  socketio.run(app, host=ARGS.host, port=ARGS.port, debug=ARGS.debug)
