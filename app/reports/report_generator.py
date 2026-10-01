class ReportGenerator:

    def generate_report(self, incidents):

        print()
        print("=" * 50)
        print("       CYBERSECURITY INCIDENT REPORT")
        print("=" * 50)

        print("Total Incidents:", len(incidents))

        print()

        for incident in incidents:

            print("Incident ID :", incident["incident_id"])
            print("Type        :", incident["incident_type"])
            print("Source IP   :", incident["source_ip"])
            print("Severity    :", incident["severity"])
            print("Status      :", incident["status"])

            print("-" * 50)