#接口监控平台
##开发过程：
`python version : 3.8.2`

安装依赖：`python3.8 -m pip install Django`

创建项目：`django-admin startproject api_platform_django`

创建app：`python manage.py startapp api_monitor`

创建虚拟环境：`python -m venv ./venv`

激活虚拟环境：`. venv/bin/active`

安装依赖：`pip install -r requirments.txt`

初始化项目：`python manage.py makemigrations`
检查项目：`python manage.py migrate`

启动项目：`python manage.py runserver`
