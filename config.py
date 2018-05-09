import os

app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL') + "?sslmode=require"
app.config['SECRET_KEY']= os.environ.get('SECRET_KEY') 
app.config['SECURITY_REGISTERABLE']= os.environ.get('SECURITY_REGISTERABLE') 
app.config['SECURITY_PASSWORD_HASH'] = os.environ.get('SECURITY_PASSWORD_HASH')  
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT') 