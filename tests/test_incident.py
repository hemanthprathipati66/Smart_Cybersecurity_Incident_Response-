import unittest

from app.models.incident import Incident
from app.exceptions.security_exceptions import InvalidSeverityError
from app.services.threat_detector import ThreatDetector


class TestIncident(unittest.TestCase):

    def test_update_severity(self):

        incident = Incident(
            "TEST001",
            "Login Attack",
            "192.168.1.20",
            "LOW"
        )

        incident.update_severity("HIGH")

        self.assertEqual(
            incident.severity,
            "HIGH"
        )

    def test_invalid_severity(self):

        incident = Incident(
            "TEST002",
            "Login Attack",
            "192.168.1.30",
            "LOW"
        )

        with self.assertRaises(InvalidSeverityError):

            incident.update_severity("INVALID")

    def test_close_incident(self):

        incident = Incident(
            "TEST003",
            "Phishing Attack",
            "192.168.1.40",
            "HIGH"
        )

        incident.close_incident()

        self.assertEqual(
            incident.status,
            "CLOSED"
        )


class TestThreatDetector(unittest.TestCase):

    def test_brute_force_detection(self):

        detector = ThreatDetector()

        event = {
            "failed_logins": 6
        }

        result = detector.detect(event)

        self.assertEqual(
            result["type"],
            "Brute Force Attack"
        )

        self.assertEqual(
            result["severity"],
            "HIGH"
        )


if __name__ == "__main__":
    unittest.main()