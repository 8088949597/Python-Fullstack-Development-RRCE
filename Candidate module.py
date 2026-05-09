from db import cursor, conn

# ---------------- Candidate Module ----------------

def candidate_register():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    sql = "INSERT INTO candidates(name,email,password) VALUES(%s,%s,%s)"
    values = (name,email,password)

    cursor.execute(sql, values)
    conn.commit()

    print("Candidate Registered Successfully")


def candidate_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    sql = "SELECT * FROM candidates WHERE email=%s AND password=%s"
    values = (email,password)

    cursor.execute(sql, values)
    user = cursor.fetchone()

    if user:
        print("Login Successful")
        candidate_menu(user[0])
    else:
        print("Invalid Credentials")


def add_skills(candidate_id):
    skills = input("Enter Skills: ")

    sql = "UPDATE candidates SET skills=%s WHERE id=%s"
    values = (skills,candidate_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Skills Updated")


def update_profile(candidate_id):
    profile = input("Enter Profile Details: ")

    sql = "UPDATE candidates SET profile=%s WHERE id=%s"
    values = (profile,candidate_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Profile Updated")


def view_jobs():
    cursor.execute("SELECT * FROM jobs WHERE status='open'")

    jobs = cursor.fetchall()

    for job in jobs:
        print(job)


def apply_job(candidate_id):
    job_id = input("Enter Job ID: ")

    sql = "INSERT INTO applications(candidate_id,job_id,status) VALUES(%s,%s,%s)"
    values = (candidate_id,job_id,"Applied")

    cursor.execute(sql, values)
    conn.commit()

    print("Applied Successfully")


def view_applied_jobs(candidate_id):
    sql = """
    SELECT jobs.title, applications.status
    FROM applications
    JOIN jobs ON applications.job_id = jobs.id
    WHERE applications.candidate_id=%s
    """

    cursor.execute(sql,(candidate_id,))

    data = cursor.fetchall()

    for d in data:
        print(d)


def withdraw_application(candidate_id):
    job_id = input("Enter Job ID to Withdraw: ")

    sql = "DELETE FROM applications WHERE candidate_id=%s AND job_id=%s"
    values = (candidate_id,job_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Application Withdrawn")


def candidate_menu(candidate_id):

    while True:
        print("\n--- Candidate Menu ---")
        print("1.Add Skills")
        print("2.Update Profile")
        print("3.View Jobs")
        print("4.Apply Job")
        print("5.View Applied Jobs")
        print("6.Withdraw Application")
        print("7.Logout")

        ch = input("Enter Choice: ")

        if ch == '1':
            add_skills(candidate_id)

        elif ch == '2':
            update_profile(candidate_id)

        elif ch == '3':
            view_jobs()

        elif ch == '4':
            apply_job(candidate_id)

        elif ch == '5':
            view_applied_jobs(candidate_id)

        elif ch == '6':
            withdraw_application(candidate_id)

        elif ch == '7':
            break

        else:
            print("Invalid Choice")


# ---------------- Company Module ----------------

def company_register():
    name = input("Enter Company Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    sql = "INSERT INTO companies(company_name,email,password) VALUES(%s,%s,%s)"
    values = (name,email,password)

    cursor.execute(sql, values)
    conn.commit()

    print("Company Registered Successfully")


def company_login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    sql = "SELECT * FROM companies WHERE email=%s AND password=%s"
    values = (email,password)

    cursor.execute(sql, values)

    company = cursor.fetchone()

    if company:
        print("Login Successful")
        company_menu(company[0])

    else:
        print("Invalid Credentials")


def post_job(company_id):
    title = input("Enter Job Title: ")
    description = input("Enter Job Description: ")

    sql = """
    INSERT INTO jobs(company_id,title,description,status)
    VALUES(%s,%s,%s,%s)
    """

    values = (company_id,title,description,"open")

    cursor.execute(sql, values)
    conn.commit()

    print("Job Posted Successfully")


def update_job(company_id):
    job_id = input("Enter Job ID: ")
    title = input("Enter New Title: ")

    sql = "UPDATE jobs SET title=%s WHERE id=%s AND company_id=%s"
    values = (title,job_id,company_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Job Updated")


def delete_job(company_id):
    job_id = input("Enter Job ID: ")

    sql = "DELETE FROM jobs WHERE id=%s AND company_id=%s"
    values = (job_id,company_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Job Deleted")


def view_applicants(company_id):
    sql = """
    SELECT applications.id, candidates.name, jobs.title
    FROM applications
    JOIN candidates ON applications.candidate_id = candidates.id
    JOIN jobs ON applications.job_id = jobs.id
    WHERE jobs.company_id=%s
    """

    cursor.execute(sql,(company_id,))

    data = cursor.fetchall()

    for d in data:
        print(d)


def shortlist_candidate():
    app_id = input("Enter Application ID: ")

    sql = "UPDATE applications SET status='Shortlisted' WHERE id=%s"

    cursor.execute(sql,(app_id,))
    conn.commit()

    print("Candidate Shortlisted")


def close_job(company_id):
    job_id = input("Enter Job ID: ")

    sql = "UPDATE jobs SET status='closed' WHERE id=%s AND company_id=%s"

    values = (job_id,company_id)

    cursor.execute(sql, values)
    conn.commit()

    print("Job Closed")


def company_menu(company_id):

    while True:

        print("\n--- Company Menu ---")
        print("1.Post Job")
        print("2.Update Job")
        print("3.Delete Job")
        print("4.View Applicants")
        print("5.Shortlist Candidate")
        print("6.Close Job")
        print("7.Logout")

        ch = input("Enter Choice: ")

        if ch == '1':
            post_job(company_id)

        elif ch == '2':
            update_job(company_id)

        elif ch == '3':
            delete_job(company_id)

        elif ch == '4':
            view_applicants(company_id)

        elif ch == '5':
            shortlist_candidate()

        elif ch == '6':
            close_job(company_id)

        elif ch == '7':
            break

        else:
            print("Invalid Choice")


# ---------------- Admin Module ----------------

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"


def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        admin_menu()

    else:
        print("Invalid Admin Credentials")


def view_candidates():
    cursor.execute("SELECT * FROM candidates")

    for c in cursor.fetchall():
        print(c)


def view_companies():
    cursor.execute("SELECT * FROM companies")

    for c in cursor.fetchall():
        print(c)


def remove_fake_user():
    user_id = input("Enter Candidate ID to Remove: ")

    sql = "DELETE FROM candidates WHERE id=%s"

    cursor.execute(sql,(user_id,))
    conn.commit()

    print("Candidate Removed")


def job_statistics():
    cursor.execute("SELECT COUNT(*) FROM jobs")

    total_jobs = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM applications")

    total_applications = cursor.fetchone()[0]

    print("Total Jobs:", total_jobs)
    print("Total Applications:", total_applications)


def generate_reports():
    cursor.execute("""
    SELECT jobs.title, COUNT(applications.id)
    FROM jobs
    LEFT JOIN applications
    ON jobs.id = applications.job_id
    GROUP BY jobs.title
    """)

    report = cursor.fetchall()

    print("\n--- Job Reports ---")

    for r in report:
        print(r)


def admin_menu():

    while True:

        print("\n--- Admin Menu ---")
        print("1.View Candidates")
        print("2.View Companies")
        print("3.Remove Fake User")
        print("4.Job Statistics")
        print("5.Generate Reports")
        print("6.Logout")

        ch = input("Enter Choice: ")

        if ch == '1':
            view_candidates()

        elif ch == '2':
            view_companies()

        elif ch == '3':
            remove_fake_user()

        elif ch == '4':
            job_statistics()

        elif ch == '5':
            generate_reports()

        elif ch == '6':
            break

        else:
            print("Invalid Choice")


# ---------------- Main Menu ----------------

while True:

    print("\n===== JOB PORTAL SYSTEM =====")
    print("1.Candidate Register")
    print("2.Candidate Login")
    print("3.Company Register")
    print("4.Company Login")
    print("5.Admin Login")
    print("6.Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        candidate_register()

    elif choice == '2':
        candidate_login()

    elif choice == '3':
        company_register()

    elif choice == '4':
        company_login()

    elif choice == '5':
        admin_login()

    elif choice == '6':
        print("Thank You")
        break

    else:
        print("Invalid Choice")