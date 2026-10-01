class ThreatDetector:

    def detect(self, event):

        failed_logins = event.get("failed_logins", 0)
        suspicious_email = event.get("suspicious_email", False)
        unusual_port = event.get("unusual_port", False)

        # Failed login detection
        if failed_logins >= 5:
            return {
                "type": "Brute Force Attack",
                "severity": "HIGH"
            }

        # Phishing detection
        if suspicious_email:
            return {
                "type": "Phishing Attack",
                "severity": "CRITICAL"
            }

        # Network detection
        if unusual_port:
            return {
                "type": "Suspicious Network Activity",
                "severity": "MEDIUM"
            }

        # No threat
        return {
            "type": "Normal Activity",
            "severity": "LOW"
        }