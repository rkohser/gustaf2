CELERY_RESULT_BACKEND = "mongodb"
CELERY_MONGODB_BACKEND_SETTINGS = {
    "host": "server",
    "port": 27017,
    "database": "gustaf_fs_backend", 
    "taskmeta_collection": "gustaf_fs_backend_meta",
}