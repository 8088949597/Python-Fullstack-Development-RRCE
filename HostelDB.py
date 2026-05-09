from pymongo import MongoClient
from datetime import date

# MongoDB connection
client = MongoClient("mongodb+srv://Kavya:Kavya8088@cluster0.ltp9tww.mongodb.net/?retryWrites=true&w=majority")
db = client["hostelDB"]

students_collection = db["students"]
complaints_collection = db["complaints"]
bookings_collection = db["bookings"]


# ---------------- STUDENT LOGIN / REGISTER ----------------
def student_login():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")

    student = students_collection.find_one({"studentId": student_id})

    if student is None:
        students_collection.insert_one({
            "studentId": student_id,
            "name": name
        })
        print("Student registered successfully!")
    else:
        print(f"Login successful. Welcome {student['name']}")

    student_menu(student_id)


# ---------------- STUDENT MENU ----------------
def student_menu(student_id):
    while True:
        print("\n===== Student Menu =====")
        print("1. Raise Complaint")
        print("2. View Complaints")
        print("3. Book Resource")
        print("4. Cancel Booking")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            raise_complaint(student_id)
        elif choice == "2":
            view_complaints(student_id)
        elif choice == "3":
            book_resource(student_id)
        elif choice == "4":
            cancel_booking(student_id)
        elif choice == "5":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice! Try again.")


# ---------------- RAISE COMPLAINT ----------------
def raise_complaint(student_id):
    complaint_type = input("Enter complaint type (Electricity / Water / Cleanliness): ")
    description = input("Enter complaint description: ")

    complaint = {
        "studentId": student_id,
        "type": complaint_type,
        "description": description,
        "status": "Pending",
        "date": str(date.today())
    }

    complaints_collection.insert_one(complaint)
    print("Complaint added successfully!")


# ---------------- VIEW STUDENT COMPLAINTS ----------------
def view_complaints(student_id):
    complaints = complaints_collection.find({"studentId": student_id})

    print("\nYour Complaints:")
    found = False
    for complaint in complaints:
        found = True
        print("-----------------------------------")
        print("Type       :", complaint["type"])
        print("Description:", complaint["description"])
        print("Status     :", complaint["status"])
        print("Date       :", complaint["date"])

    if not found:
        print("No complaints found.")


# ---------------- BOOK RESOURCE ----------------
def book_resource(student_id):
    resource = input("Enter resource (Washing Machine / Study Room / Gym Slot): ")
    time_slot = input("Enter time slot (Example: 10AM-11AM): ")
    booking_date = input("Enter booking date (YYYY-MM-DD): ")

    existing_booking = bookings_collection.find_one({
        "resource": resource,
        "timeSlot": time_slot,
        "date": booking_date
    })

    if existing_booking:
        print("Slot already booked! Choose another time.")
        return

    booking = {
        "resource": resource,
        "studentId": student_id,
        "timeSlot": time_slot,
        "date": booking_date
    }

    bookings_collection.insert_one(booking)
    print("Resource booked successfully!")


# ---------------- CANCEL BOOKING ----------------
def cancel_booking(student_id):
    resource = input("Enter resource to cancel: ")
    time_slot = input("Enter time slot: ")
    booking_date = input("Enter date (YYYY-MM-DD): ")

    result = bookings_collection.delete_one({
        "studentId": student_id,
        "resource": resource,
        "timeSlot": time_slot,
        "date": booking_date
    })

    if result.deleted_count > 0:
        print("Booking cancelled successfully!")
    else:
        print("No matching booking found.")


# ---------------- ADMIN LOGIN ----------------
def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == "admin" and password == "admin123":
        print("Admin login successful!")
        admin_menu()
    else:
        print("Invalid admin credentials!")


# ---------------- ADMIN MENU ----------------
def admin_menu():
    while True:
        print("\n===== Admin Menu =====")
        print("1. View Complaints")
        print("2. Update Complaint Status")
        print("3. View Bookings")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            view_all_complaints()
        elif choice == "2":
            update_complaint_status()
        elif choice == "3":
            view_all_bookings()
        elif choice == "4":
            print("Admin logged out successfully.")
            break
        else:
            print("Invalid choice! Try again.")


# ---------------- VIEW ALL COMPLAINTS ----------------
def view_all_complaints():
    complaints = complaints_collection.find()

    print("\nAll Complaints:")
    found = False
    for complaint in complaints:
        found = True
        print("-----------------------------------")
        print("Student ID  :", complaint["studentId"])
        print("Type        :", complaint["type"])
        print("Description :", complaint["description"])
        print("Status      :", complaint["status"])
        print("Date        :", complaint["date"])

    if not found:
        print("No complaints found.")


# ---------------- UPDATE COMPLAINT STATUS ----------------
def update_complaint_status():
    student_id = int(input("Enter Student ID: "))
    description = input("Enter complaint description: ")

    complaint = complaints_collection.find_one({
        "studentId": student_id,
        "description": description
    })

    if complaint:
        print("Current Status:", complaint["status"])
        new_status = input("Enter new status (Pending / In Progress / Resolved): ")

        complaints_collection.update_one(
            {"studentId": student_id, "description": description},
            {"$set": {"status": new_status}}
        )

        print("Complaint status updated successfully!")
    else:
        print("Complaint not found.")


# ---------------- VIEW ALL BOOKINGS ----------------
def view_all_bookings():
    bookings = bookings_collection.find()

    print("\nAll Bookings:")
    found = False
    for booking in bookings:
        found = True
        print("-----------------------------------")
        print("Resource   :", booking["resource"])
        print("Student ID :", booking["studentId"])
        print("Time Slot  :", booking["timeSlot"])
        print("Date       :", booking["date"])

    if not found:
        print("No bookings found.")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n===== College Hostel Complaint & Resource Booking System =====")
        print("1. Student Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_login()
        elif choice == "2":
            admin_login()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()