role = input("Enter your role: ").strip().lower()

student = {}

if role == "student":
    try:
        user_id = int(input("Enter your USER ID:\n"))
        full_name = str(input("Enter your full name:\n"))
        email = input("Enter your email:\n")
        password_hash = input("Enter your password:\n")

        student = {
            "ID": user_id,
            "name": full_name,
            "Email": email,
            "password": password_hash
        }
    except ValueError:
        print("Error in details entered (one of the details is incorrect)!")



   
    



