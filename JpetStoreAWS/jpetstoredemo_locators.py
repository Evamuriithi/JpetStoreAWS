import datetime
from faker import Faker
fake = Faker(locale='en_US')

app = 'jpetstoredemo'
jpetstoredemo_url = 'https://petstore.octoperf.com/actions/Account.action?signonForm='
jpetstoredemo_home_page_title = 'JPetStore Demo'
jpetstoredemo_login_page_url = 'https://petstore.octoperf.com/actions/Account.action?signonForm='

sysid = ''
new_username = fake.user_name()
new_password = fake.password()
#username = fake.new_username()
password1 = fake.password()
password2 = fake.password()
first_name = fake.first_name()
last_name = fake. last_name()
phonenum = fake.phone_number()
address1 = fake.address().replace("\n"," ")
address2 = fake.address().replace("\n"," ")
email = fake.email()
country = fake.country()
city = fake.city()
state = fake.state()[0:10]
zip_code = fake.zipcode()[0:10]

