from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = '5943068483:AAEXfh7Sw0dWjvXfaABa4I86-JXJ2rAE7v4'  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
