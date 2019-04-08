from wsgiref.simple_server import make_server

# import function which connects to the database and returns a list of restaurants
from database_connect import get_restaurants

#useful for parsing the post request from wsgi 
from urllib import parse

## first view: ask for the neighborhood. 
# this is static HTML, which containts a form. 
def index():
    html = """
    <html>
    <head>
    <title>A super simple python WSGI server</title>
    </head>
    <body>

    <p>
    This is a simple Python WSGI server. This html generated from a function. 
    </p>
    <form action="" method="post">
    </form>
    </body>
    </html>
    """

    return [html.encode("utf-8")]


    if __name__ == '__main__':
    
    print("Staring restaurants website server.")

    PORT = 8000
    ADDRESS = 'localhost'

    # define server daemon, which takes the main application function define above as an argument.
    httpd = make_server(ADDRESS, PORT, neighborhood_restaurants)
    print("WSGI Server running on port http://{address_placeholder}:{port_placeholder}".format(address_placeholder=ADDRESS, port_placeholder=PORT))

    # server
    httpd.serve_forever()