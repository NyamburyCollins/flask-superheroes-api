# flask-superheroes-api
# Flask Superheroes API

## Description
A Flask API for tracking superheroes and their powers. Built as part of the Phase 4 Code Challenge at Flatiron School.


## Setup
```bash
git clone <https://github.com/NyamburyCollins/flask-superheroes-api>
cd flask-superheroes-api
pip install -r requirements.txt
flask db upgrade
python seed.py
flask run

 

## 📦 Features

- View a list of heroes and their powers
- Add new hero powers with validations
- Update power descriptions
- Built with Flask, SQLAlchemy, and SQLite
- RESTful endpoints with JSON responses

---

## 🚀 Getting Started

### 📁 Clone the Repository

```bash
git clone <https://github.com/NyamburyCollins/flask-superheroes-api>/flask-superheroes-api.git
cd flask-superheroes-api
🐍 Create and Activate a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🧱 Database Setup
1. Initialize the DB
bash
Copy
Edit
flask db init
2. Create Migration Files
bash
Copy
Edit
flask db migrate -m "Initial migration"

3. Apply Migrations
bash
Copy
Edit
flask db upgrade

4. Seed the Database
bash
Copy
Edit
python seed.py
 Running the Server
bash
Copy
Edit
flask run

Then access the API at:
http://127.0.0.1:5000

 API Endpoints
GET /heroes
Returns a list of all heroes.

GET /heroes/:id
Returns one hero and their powers.

GET /powers
Returns a list of all powers.

GET /powers/:id
Returns one power by ID.

PATCH /powers/:id
Updates a power’s description.

POST /hero_powers
Creates a new HeroPower record (with validation).

✅ Validations
Power.description must be present and at least 20 characters

HeroPower.strength must be one of: "Strong", "Weak", "Average"

📂 Project Structure
arduino
Copy
Edit
.
├── app.py
├── models.py
├── routes.py
├── config.py
├── seed.py
├── requirements.txt
├── migrations/
└── README.md
👤 Author
Collins Nyambury

GitHub: https://github.com/NyamburyCollins/flask-superheroes-api

📧 Support
For help or suggestions, feel free to open an issue.

📄 License
This project is for educational purposes.

yaml
Copy
Edit

---

