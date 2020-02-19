# Example class to start a Waitress server as a windows service
# the specific use case is running Waitress as a windows server using pywin32
# The Waitress docs only show how to use waitress-serve, but since waitress-serve is blocking
# you don't get a return value, which makes it impossible to gracefully stop the Waitress server
# from a windows service
# However, looking at the waitress-serve code, it's easy to write a custom class

# example pywin32 windows service: https://gist.github.com/drmalex07/10554232

from waitress.server import create_server


class WaitressServer:

    def __init__(self, app, host, port):
        """
        initiate waitress server object
        :param app: Flask app object
        :param host: IP of host
        :param port: target port
        """
        self.server = create_server(app, host=host, port=port)

    def run(self):
        """ call this method from your service to start the Waitress server """
        self.server.run()

    def stop_service(self):
        """ call this method from the services stop method """
        self.server.close()


if __name__ == "__main__":
    from myapp import app
    host = "localhost"
    port = "9090"
    print("server starting on {}:{}".format(host, port))
    server = WaitressServer(app, "localhost", "9090")
    server.run()
