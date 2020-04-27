# Get user email address
email = input("What is your email address?: ")
print(email)

# Slice out the user name (you can use find or index)
user_name = email[:email.find("@")]

# Slice the domain name
domain_name = email[email.find("@")+1:]

# Format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)