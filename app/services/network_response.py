from app.services.incident_response import IncidentResponse


class NetworkResponse(IncidentResponse):

    def respond(self):
        print("Network Response: Blocking suspicious network activity.")