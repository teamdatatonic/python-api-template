from src.hello import hello

import flask
import logging
import os


#######################################
# Globals
#######################################
# Setup logging
logging.basicConfig(level=eval(f"logging.{os.getenv('LOG_LEVEL', 'INFO')}"))

# Flask app
app = flask.Flask(__name__)

#######################################
# Endpoints
#######################################

@app.endpoint("API_serve")
def api_serve() -> tuple:
    logging.info(f"API_serve Stub")

    # TODO: plug in request to Vertex Serving API here :) 

    return flask.jsonify({"response": {"message": hello()}})



#######################################
# Routes
#######################################

# API Serve
if os.getenv("API_SERVE_ENABLED", "false").lower() == "true":
    api_route_name:str = os.getenv('API_SERVE_ROUTE', '/api/v1/serve')
    app.logger.info("Enabling API Serve Endpoint")
    app.add_url_rule(
        api_route_name, 
        methods=['POST'],
        endpoint="API_serve"
    )

# Health check
@app.route("/healthz", methods=["GET"])
def health_check() -> tuple:
    return (flask.jsonify({"success": True}), 200)

#######################################
# Response Security modifiers
#######################################
@app.after_request
def apply_additional_security_headers(response):
    response.headers["X-Permitted-Cross-Domain-Policies"] = "none"
    response.headers["Cache-control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    return response

#######################################
# Entrypoint
#######################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
