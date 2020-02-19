from service_base import SMWinservice
from waitress_server import WaitressServer
from myapp import app

HOST = "localhost"
PORT = "9090"

server = WaitressServer(app, HOST, PORT)


class DemoService(SMWinservice):
    _svc_name_ = "DemoService"
    _svc_display_name_ = "Demo Service"
    _svc_description_ = "Demo service! Running on Port {}".format(PORT)

    def start(self):
        """
        if required, add custom action here
        will happen before service log message
        """
        pass

    def stop(self):
        server.stop_service()

    def main(self):
        server.run()


if __name__ == '__main__':
    DemoService.parse_command_line()
