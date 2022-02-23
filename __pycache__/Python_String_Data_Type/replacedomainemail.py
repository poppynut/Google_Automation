def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index=email.index("@" + old_domain)
        new_email=email[:index] + "@" + new_domain #First Portion of the Old email up until the index we have calculated.
        return new_email
    return email

print(replace_domain("raj@google.com", "google.com", "linux.com" ))