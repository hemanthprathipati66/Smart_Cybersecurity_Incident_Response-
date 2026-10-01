from app.exceptions.security_exceptions import InvalidSeverityError


class Incident:

    def __init__(self, incident_id, incident_type, source_ip, severity):
        self.__incident_id = incident_id
        self.__incident_type = incident_type
        self.__source_ip = source_ip
        self.__severity = severity
        self.__status = "OPEN"

    @property
    def incident_id(self):
        return self.__incident_id

    @property
    def incident_type(self):
        return self.__incident_type

    @property
    def source_ip(self):
        return self.__source_ip

    @property
    def severity(self):
        return self.__severity

    @property
    def status(self):
        return self.__status

    def display(self):
        print("Incident ID :", self.__incident_id)
        print("Type        :", self.__incident_type)
        print("Source IP   :", self.__source_ip)
        print("Severity    :", self.__severity)
        print("Status      :", self.__status)

    def update_severity(self, severity):

        valid_severities = [
            "CRITICAL",
            "HIGH",
            "MEDIUM",
            "LOW"
        ]

        if severity in valid_severities:
            self.__severity = severity
        else:
            raise InvalidSeverityError(
                f"Invalid severity: {severity}"
            )

    def close_incident(self):
        self.__status = "CLOSED"