from app.models.incident import Incident


class NetworkIncident(Incident):

    def __init__(self, incident_id, source_ip, severity, port):
        super().__init__(
            incident_id,
            "Network Attack",
            source_ip,
            severity
        )

        self.__port = port

    def display(self):
        super().display()
        print("Port        :", self.__port)