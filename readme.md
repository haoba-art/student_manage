# 使用说明

### 1. 配置settings

settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stu',  # 数据库名字
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
    }
}
```

### 2. model迁移

python manage.py migrate 

### 3. 注意安装必备的库

pip intall -r requirments.txt