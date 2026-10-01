class ResponseEngine:

    def respond(self, incident):

        if incident.incident_type == "Brute Force Attack":
            print("Response Action: Blocking suspicious IP address.")

        elif incident.incident_type == "Phishing Attack":
            print("Response Action: Blocking malicious email.")

        elif incident.incident_type == "Suspicious Network Activity":
            print("Response Action: Blocking suspicious network activity.")

        else:
            print("Response Action: Monitoring the incident.")