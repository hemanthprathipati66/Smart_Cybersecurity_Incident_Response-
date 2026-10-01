from app.models.incident import Incident


class PhishingIncident(Incident):

    def __init__(self, incident_id, source_ip, severity, email):
        super().__init__(
            incident_id,
            "Phishing Attack",
            source_ip,
            severity
        )

        self.__email = email

    def display(self):
        super().display()
        print("Email       :", self.__email)