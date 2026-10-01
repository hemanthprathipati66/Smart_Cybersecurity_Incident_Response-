from app.models.incident import Incident
from app.models.network_incident import NetworkIncident
from app.models.phishing_incident import PhishingIncident
from app.exceptions.security_exceptions import InvalidSeverityError
from app.services.network_response import NetworkResponse
from app.services.phishing_response import PhishingResponse
from app.services.threat_detector import ThreatDetector
from app.services.incident_service import IncidentService
from app.services.response_engine import ResponseEngine
from app.services.incident_storage import IncidentStorage
from app.reports.report_generator import ReportGenerator
from app.reports.incident_statistics import IncidentStatistics


# Normal Incident

incident1 = Incident(
    "INC001",
    "Suspicious Login",
    "192.168.1.10",
    "HIGH"
)

incident2 = Incident(
    "INC002",
    "Phishing Attempt",
    "10.0.0.25",
    "MEDIUM"
)


# Update severity

incident1.update_severity("CRITICAL")


# Test invalid severity

try:
    incident2.update_severity("ABC")
except InvalidSeverityError as e:
    print("Security Error:", e)


# Close incident

incident2.close_incident()


# Display incidents

print()

incident1.display()

print()

incident2.display()


# Network Incident

print()

network_incident = NetworkIncident(
    "INC003",
    "192.168.1.50",
    "HIGH",
    443
)

network_incident.display()


# Phishing Incident

print()

phishing_incident = PhishingIncident(
    "INC004",
    "10.10.10.20",
    "CRITICAL",
    "attacker@gmail.com"
)

phishing_incident.display()


# Polymorphism

def process_incident(incident):
    print("\nProcessing Incident:")
    incident.display()


process_incident(network_incident)
process_incident(phishing_incident)


# Abstraction

network_response = NetworkResponse()
phishing_response = PhishingResponse()

print()

network_response.respond()
phishing_response.respond()


# Threat Detection

detector = ThreatDetector()

event1 = {
    "failed_logins": 6
}

result1 = detector.detect(event1)

print()

print("Threat Detection Result:")
print("Threat   :", result1["type"])
print("Severity :", result1["severity"])


# Automatic Incident Creation

incident_service = IncidentService()

new_incident = incident_service.create_incident(
    "INC005",
    "192.168.1.100",
    result1
)

print()

print("Automatically Created Incident:")
new_incident.display()


# Response Engine

response_engine = ResponseEngine()

print()

print("Automated Response:")

response_engine.respond(new_incident)


# Incident Storage

storage = IncidentStorage()

print()

storage.save_incident(new_incident)


# Load Stored Incidents

print()

print("Stored Incidents:")

stored_incidents = storage.load_incidents()

for incident in stored_incidents:

    print(
        incident["incident_id"],
        "|",
        incident["incident_type"],
        "|",
        incident["source_ip"],
        "|",
        incident["severity"],
        "|",
        incident["status"]
    )


# Incident Report

report_generator = ReportGenerator()

report_generator.generate_report(stored_incidents)


# Incident Statistics

statistics = IncidentStatistics()

statistics.generate_statistics(stored_incidents)