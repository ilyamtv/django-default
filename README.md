django-default
==============

### Install
pip install django-endless-pagination  
pip install south  
pip install django-mptt   
pip install django-annoying   

### Windows install
copy .gitignore.tpl .gitignore  
cd project  
copy settings_dev.py.tpl settings_dev.py  
copy manage_dev.py.tpl manage_dev.py  
Configure database connection in settings_dev.py
python manage.py syncdb  
python manage.py migrate  
python manage.py runserver  
Enjoy)  