from resource import *

@app.route('/shutdown', methods=['GET'])
@app.route('/turnoff', methods=['GET'])
@app.route('/off', methods=['GET'])
def shutdown(): 
    """Renders the shutdown page."""
    try:
        func = request.environ.get('werkzeug.server.shutdown')
        if(func is None):
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
    except:
        app.socketio.stop()
    return 'Server shutting down...'

