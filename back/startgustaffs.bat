TITLE gustafFS
call "venv\Scripts\activate.bat"
celery -A fs.gustaffs worker --loglevel=debug