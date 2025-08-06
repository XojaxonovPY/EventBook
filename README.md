# 🎉 Event Booking API

Event Booking API — foydalanuvchilarga o‘z tadbirlarini tashkil qilish va boshqalar bu tadbirlarga ro‘yxatdan o‘tishi
mumkin bo‘lgan RESTful API.

---

## 📌 Loyihaning vazifasi

Foydalanuvchilar:

- Ro‘yxatdan o‘tishi va login qilishi mumkin
- O‘z tadbirlarini yaratishi
- Tadbirga ro‘yxatdan o‘tishi
- O‘z tadbirlari va qatnashayotgan tadbirlarini ko‘rishi mumkin

---

## ⚙️ Texnologiyalar

- Python 3.11+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (JWT autentifikatsiya uchun)
- SQLite (yoki PostgreSQL)
- drf-spectacular (Swagger uchun)

---

## 🚀 Loyihani ishga tushirish

### 🔽 Klonlash:

```bash
git clone https://github.com/USERNAME/EventBookingAPI.git
cd EventBookingAPI
```

### 🛠 Virtual muhit yaratish:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 📦 Kutubxonalarni o‘rnatish:

```bash
pip install -r requirements.txt
```

### 🗃 Migratsiyalar:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 👤 Superuser yaratish (admin panel uchun):

```bash
python manage.py createsuperuser
```

### 🟢 Serverni ishga tushirish:

```bash
python manage.py runserver
```

### 🔍 Swagger (API hujjatlari):

```text
http://localhost:8000/api/schema/swagger-ui/
```

---

## 🔐 API Endpointlar

| Endpoint                             | Method | Tavsif                                            |
|--------------------------------------|--------|---------------------------------------------------|
| `/api/v1/register/`                  | POST   | Yangi foydalanuvchini ro‘yxatdan o‘tkazish        |
| `/api/v1/login/`                     | POST   | JWT token olish                                   |
| `/api/v1/token/refresh/`             | POST   | Access tokenni yangilash                          |
| `/api/v1/list/events/`               | GET    | Barcha tadbirlar ro‘yxati                         |
| `/api/v1/create/event/`              | POST   | Yangi tadbir yaratish (faqat login foydalanuvchi) |
| `/api/v1/events/{id}/`               | GET    | Bitta tadbir tafsilotlari                         |
| `/api/v1/registeration/event/`       | POST   | Tadbirga ro‘yxatdan o‘tish (login foydalanuvchi)  |
| `/api/v1/list/user/event/`           | GET    | Foydalanuvchi yaratgan tadbirlar                  |
| `/api/v1/user/register/event/list/'` | GET    | Foydalanuvchi qatnashayotgan tadbirlar            |

---

## 🔑 Autentifikatsiya

Loyiha `JWT` orqali foydalanuvchini autentifikatsiya qiladi. Har bir himoyalangan endpoint uchun `Authorization`
headerda `access token` yuboriladi:

```
Authorization: Bearer <access_token>
```

---

## 👨‍💻 Muallif

- Ism: Joker Xojaxonov
- GitHub: [https://github.com/XojaxonovPY](https://github.com/XojaxonovPY)

---

## 📌 Eslatma

Bu loyiha o‘quv va test maqsadlarida yozilgan. Production versiyada quyidagi sozlamalar alohida ko‘rib chiqilishi kerak:

- `DEBUG = False`
- `HTTPS`
- `CORS`
- `Deployment (Docker, Render, Railway)`
