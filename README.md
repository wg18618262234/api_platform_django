#接口监控平台
django文档：
https://docs.djangoproject.com/
https://docs.djangoproject.com/zh-hans/3.1/topics/
##开发过程：
`python version : 3.7.9`

安装依赖：`python3.7 -m pip install Django`

创建项目：`django-admin startproject api_platform_django`

创建app：`python manage.py startapp api_monitor`

创建虚拟环境：`virtualenv venv`

激活虚拟环境：`. venv/bin/active`

pip换源：`pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/`,`pip config set install.trusted-host mirrors.aliyun.com`

安装依赖：`pip install -r requirments.txt`

为模型生成迁移文件：`python manage.py makemigrations ApiMonitorConfig`

查看迁移命令的sql：`python manage.py sqlmigrate api_monitor 0001`

应用数据库迁移：`python manage.py migrate`

检查项目问题：`python manage.py check`

启动项目：`python manage.py runserver`

启用shell模式：`python manage.py shell`

创建admin登录账号：`python manage.py createsuperuser`

启动redis：`redis-server`

启动celery：`celery -A api_platform_django worker -B -l info`