def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index=email.index("@" + old_domain)
        print(index)
        new_email=email[:index] + "@" + new_domain
        return new_email
    return email


print(replace_domain("raj@gmail.com", "gmail.com", "rk.com"))