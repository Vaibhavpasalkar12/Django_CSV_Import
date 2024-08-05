# User-Friendly CSV File Uploader with Data Analysis and Visualization

### Technologies Used: Django, Python, Pandas, Matplotlib, seaborn, HTML+CSS

# Setup Instructions:
## Prerequisites:
1) Python 3.x
2) Django 
3) Virtualenv (optional but recommended)

### Step 1: Clone the Repository
git clone (https://github.com/Vaibhavpasalkar12/Django_CSV_Import.git)
cd your-repository
### Step 2: Create and Activate a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
### Step 3: Install Dependencies
pip install -r requirements.txt
### Step 4: Apply Migrations
python manage.py migrate
### Step 5: Create a Superuser (to access Django Admin)
python manage.py createsuperuser
### Step 6: Run the Development Server
python manage.py runserver . 
Visit http://127.0.0.1:8000/ in your web browser to access the application.
### Step 7: Access the Admin Interface
Visit http://127.0.0.1:8000/admin in your web browser and log in with the superuser credentials you created earlier.
