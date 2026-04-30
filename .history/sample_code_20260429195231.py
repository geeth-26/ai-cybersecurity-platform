password = "12345"

query = "SELECT * FROM users WHERE name = '" + user + "'"

print("<script>alert('XSS')</script>")