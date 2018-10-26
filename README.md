Django Modern Admin Sample
===================

Sample project for django_modern_admin.

Quick start
-----------

![alt text](https://raw.githubusercontent.com/arifonursen/django_modern_admin/master/login.png)
![alt text](https://raw.githubusercontent.com/arifonursen/django_modern_admin/master/dashboard1.png)
![alt text](https://raw.githubusercontent.com/arifonursen/django_modern_admin/master/dashboard2.png)
![alt text](https://raw.githubusercontent.com/arifonursen/django_modern_admin/master/dashboard3.png)
![alt text](https://raw.githubusercontent.com/arifonursen/django_modern_admin/master/datefield.png)
![alt text](https://raw.githubusercontent.com/arifonursen/django_modern_admin/master/recent.png)

1. You must create new environment and install requirements.txt

2. Run `python manage.py migrate` to create the database.

3. You must define in settings.py 
	```
	GOOGLE_ANALYTICS_SERVICE_ACCOUNT_JSON = os.path.join(BASE_DIR, ‘xxx.json’)
	
	GOOGLE_ANALYTICS_ID = ‘123456789’
	```

4. Visit http://127.0.0.1:8000/admin/

