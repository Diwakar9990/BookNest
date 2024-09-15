========== vue / Frontend ==========

#1 Open frontend folder
   -> cd /frontend

#2 Install all dependencies
   -> npm i  

#3 Run the vue application
   -> npm run serve


========== Flask / Backend ==========

#1 Open backend folder
   -> cd /Backend

  ---  Linux  --- 
#2 Create vertual enviorment (linux)
   -> virtualenv env

#3 Activate virtual enviorment (linux)
   -> . env/bin/activate

  ---  windows  --- 
#2 Create vertual enviorment (windows)
   -> python -m venv env   

#3 Activate virtual enviorment  (windows)
   -> env/Scripts/activate 

#4 Download all flask modules
   -> pip install -r requirements.txt

#5 Run the application
   -> flask run 

========== Redis & Celery ==========

#1 Start the redis server
   -> sudo snap start redis

#2 Celery task worker command
   -> celery -A tasks worker --loglevel=info -P eventle

#3 Celery task scheduler command
   -> celery -A tasks scheduler --loglevel=info
