import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split input on comma or whitespace
        parts = re.split(r'[,\s]+', self.addresses.strip())

        # Define a basic email regex
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

        # Filter only valid emails and remove duplicates
        unique_emails = {email for email in parts if email_pattern.fullmatch(email)}

        # Return sorted list
        return sorted(unique_emails)
