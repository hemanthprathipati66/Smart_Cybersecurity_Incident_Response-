from app.services.incident_response import IncidentResponse


class PhishingResponse(IncidentResponse):

    def respond(self):
        print("Phishing Response: Blocking malicious email.")