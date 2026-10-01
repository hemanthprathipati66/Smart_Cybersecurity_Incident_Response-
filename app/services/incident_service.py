from app.models.incident import Incident


class IncidentService:

    def create_incident(self, incident_id, source_ip, threat_result):

        incident = Incident(
            incident_id,
            threat_result["type"],
            source_ip,
            threat_result["severity"]
        )

        return incident