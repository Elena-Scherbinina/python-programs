# Kanban Manager
This project was developed as part of the UCSC Extension Software Engineering & QA certification.
It is a Django REST API for managing Kanban cards and tasks.

1. Features \
✅ CRUD operations for Kanban cards and tasks \
✅ Basic authentication (users can only manage their own cards) \
✅ Many-to-one relationship: each Kanban card can have multiple tasks \
✅ Status choices: to-do, in-progress, done \
✅ Nested task structure in API responses \
✅ Automated tests with pytest

2. Requirements \
Before running the project, make sure you have:

   Python 3.x installed \
   The following Python libraries:
  - django
  - djangorestframework
  - pytest
  - pytest-django

3. Setup
 - git clone https://github.com/Elena-Scherbinina/python-programs.git
 - cd python-programs/certification/django-rest-api/kanban-manager

 - pip install django djangorestframework pytest pytest-django


4. Run Database Migrations
 - python manage.py migrate

5. Run the Django Development Server
 - python manage.py runserver
   API should now be running at http://127.0.0.1:8000/

6. API Endpoints \
  Kanban Cards \
  GET /cards/ → List all cards \
  POST /cards/ → Create a new card \
  GET /cards/<id>/ → Retrieve a specific card \
  PUT /cards/<id>/ → Update a card \
  DELETE /cards/<id>/ → Delete a card

     Tasks (Nested in Cards) \
     GET /cards/ → Returns tasks inside each card \
     GET /tasks/<id>/ → Retrieves a task (shows only card_id)


  Example API Response: \
  [ { \
      "id": 1, \
      "title": "Project Setup", \
      "description": "Initialize project repository", \
      "status_text": "to-do", \
      "tasks": [ \
        { \
         "id": 1, \
         "description": "Create Django project", \
         "done": false, \
         "card": 1 \
        }] \
    }]

7. Authentication
 -  Only authenticated users can manage their own Kanban cards and tasks.
 -  Users must be manually created in the Django shell


6. Running Tests \
    pytest \
    ✅ Anonymous users cannot create Kanban cards (401 Unauthorized) \
    ✅ Authenticated users can create cards (201 Created).
