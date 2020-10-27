# Combining the previously written regex
valid_email = re.compile("([a-zA-Z]+\.[a-zA-Z]+)@([a-zA-Z]+)(.gov.uk)$")

# Create new column containing match info
gov_emails["match"] = gov_emails["email"].str.match(valid_email)

# Check results
print("Number of incorrect matches:", (gov_emails["should_match"] != gov_emails["match"]).sum())

gov_emails