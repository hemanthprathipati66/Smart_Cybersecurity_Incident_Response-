class IncidentStatistics:

    def generate_statistics(self, incidents):

        total = len(incidents)

        open_incidents = 0
        closed_incidents = 0

        critical = 0
        high = 0
        medium = 0
        low = 0

        for incident in incidents:

            if incident["status"] == "OPEN":
                open_incidents += 1

            elif incident["status"] == "CLOSED":
                closed_incidents += 1

            if incident["severity"] == "CRITICAL":
                critical += 1

            elif incident["severity"] == "HIGH":
                high += 1

            elif incident["severity"] == "MEDIUM":
                medium += 1

            elif incident["severity"] == "LOW":
                low += 1

        print()
        print("=" * 50)
        print("          INCIDENT STATISTICS")
        print("=" * 50)

        print("Total Incidents    :", total)
        print("Open Incidents     :", open_incidents)
        print("Closed Incidents   :", closed_incidents)

        print()

        print("Critical Incidents :", critical)
        print("High Incidents     :", high)
        print("Medium Incidents   :", medium)
        print("Low Incidents      :", low)

        print("=" * 50)