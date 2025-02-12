MySQL Database Password Rotation Script
This is a DevOps & Security Automation project that automates password rotation for MySQL using Python and subprocess. This is a Database Password Rotation Script in Python.

📌 Project Overview
What it does:
✅ Generates a random new password
✅ Connects to MYsql via subprocess
✅ Runs a Mtsql query to update the password
✅ Stores the new password securely (optional: AWS Secrets Manager, Vault, or a local file)
 
 
 This is actually a real-world DevOps use case! 🎯

Why?

Automating Password Rotation 🔄

Many security policies require regular password rotation for databases.
Your script automates the process, reducing manual work.
Securely Storing Credentials 🔐

Instead of manually remembering passwords, they are stored in a secure file.
Can be extended to use environment variables or secret vaults like AWS Secrets Manager or HashiCorp Vault.
Using Scripting for Admin Tasks ⚙️

DevOps engineers automate database admin tasks to improve efficiency.
This script could be integrated into CI/CD pipelines for database access management.


Required Libraries:

subprocess → To execute MongoDB queries
string, secrets → To generate random passwords



📂 How to Use
1️⃣ Clone the repository:

git clone https://github.com/11-Sarthak/mysqlDatabase-password-rotation.git
cd mysqlDatabase-password-rotation

2️⃣ Run the script:
python password_rotation.py

3️⃣ Enter MySQL credentials when prompted

Author
Sarthak
