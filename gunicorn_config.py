command = '/home/mtkg/code/ar-mt-kg/env/bin/gunicorn'
pythonpath = '/home/mtkg/code/ar-mt-kg'
bind = '127.0.0.1:8001'
workers = 5
timeout = 6000
user = 'mtkg'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=web_mtkg.settings'
