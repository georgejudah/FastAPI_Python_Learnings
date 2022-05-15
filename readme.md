Setup
1.py -3 -m venv venv
2.venv\Scripts\activate
3.pip install -r requirements.txt
4.uvicorn app:app --reload
#in the above unicorn command, first instance of app refers to file name, second refers to the object of the FastAPI class created in app.py file