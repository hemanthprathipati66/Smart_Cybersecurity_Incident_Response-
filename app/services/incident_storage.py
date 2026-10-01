import json
import os


class IncidentStorage:

    def __init__(self, file_path="data/incidents.json"):
        self.file_path = file_path

    def save_incident(self, incident):

        data = []

        if os.path.exists(self.file_path):

            with open(self.file_path, "r") as file:

                try:
                    data = json.load(file)

                except json.JSONDecodeError:
                    data = []

        # Check duplicate incident ID

        for existing_incident in data:

            if existing_incident["incident_id"] == incident.incident_id:
                print("Incident already exists:", incident.incident_id)
                return

        incident_data = {
            "incident_id": incident.incident_id,
            "incident_type": incident.incident_type,
            "source_ip": incident.source_ip,
            "severity": incident.severity,
            "status": incident.status
        }

        data.append(incident_data)

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("Incident saved successfully.")

    def load_incidents(self):

        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as file:

            try:
                return json.load(file)

            except json.JSONDecodeError:
                return []