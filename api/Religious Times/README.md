# 🕌 Religious Times API
### نسخه: Religious Times API v1.0.0

وب‌سرویس **Religious Times API** یک API سریع، سبک و بدون نیاز به API Key برای  
🕋 **دریافت اوقات شرعی و اطلاعات مکانی شهرهای ایران** است.

این سرویس با دریافت نام شهر، موقعیت جغرافیایی و اوقات شرعی همان روز را  
به‌صورت استاندارد و ساخت‌یافته **JSON** برمی‌گرداند.

🔹 بدون نیاز به API Key  
🔹 مناسب ربات‌ها، وب‌سایت‌ها و اپلیکیشن‌های موبایل  
🔹 شامل اطلاعات کامل اوقات شرعی، تاریخ شمسی، قمری و میلادی  

---

## 🧠 نحوه کار API (Architecture)

1️⃣ کلاینت نام شهر را ارسال می‌کند  
2️⃣ سرور موقعیت جغرافیایی شهر را تشخیص می‌دهد  
3️⃣ اوقات شرعی بر اساس مختصات محاسبه می‌شود  
4️⃣ خروجی نهایی به‌صورت JSON بازگردانده می‌شود  

---

## 🌐 آدرس اصلی وب‌سرویس

https://abolfazlzarei.sbs/ReligiousTimes.php

---

## 🔗 Endpoint

### 🔹 دریافت اوقات شرعی شهر

```http
GET /oghat?q={CITY_NAME}
```

## 📌 پارامتر ورودی

| پارامتر | نوع | توضیح |
|--------|-----|-------|
| `q` | `string` | نام شهر (مثال: مشهد، تهران، قم) |

---


# 🧪 نمونه درخواست

```http
GET https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=مشهد
```

---

# 📦 ساختار خروجی API

```json
{
    "status": 200,
    "message": "اطلاعات با موفقیت دریافت شد",
    "data": {
        "location": {
            "coordinates": {
                "latitude": "179.87",
                "longitude": "259.2"
            },
            "address_parts": [
                "مشهد",
                "استان خراسان رضوی"
            ],
            "city": "مشهد",
            "province": "استان خراسان رضوی",
            "full_address": "مشهد, استان خراسان رضوی"
        },
        "prayer_times": {
            "status": 200,
            "out": {
                "Fajr": "05:08",
                "Sunrise": "06:35",
                "Dhuhr": "11:45",
                "Asr": "14:33",
                "Sunset": "16:54",
                "Maghrib": "17:14",
                "Isha": "18:03",
                "Midnight": "23:01",
                "FFajr": "05:07",
                "FSunrise": "06:34",
                "ym": 2026,
                "mm": 1,
                "dm": 29,
                "yg": 1447,
                "mg": "شعبان",
                "dg": 9,
                "ds": 9,
                "ys": 1404,
                "ms": 11,
                "week": "پنجشنبه",
                "l1": "179.87",
                "l2": "259.2"
            }
        }
    },
    "developer": "@Ninga_code",
    "timestamp": "2026-01-29T09:10:28+00:00"
}
```


---


## 🧾 توضیح فیلدهای مهم خروجی

### 📍 Location

| فیلد | توضیح |
|------|-------|
| `latitude` | عرض جغرافیایی |
| `longitude` | طول جغرافیایی |
| `city` | نام شهر |
| `province` | نام استان |
| `full_address` | آدرس کامل تشخیص داده‌شده |

---

### 🕰 Prayer Times

| فیلد | توضیح |
|------|-------|
| `Fajr` | اذان صبح |
| `Sunrise` | طلوع آفتاب |
| `Dhuhr` | اذان ظهر |
| `Asr` | اذان عصر |
| `Sunset` | غروب |
| `Maghrib` | اذان مغرب |
| `Isha` | اذان عشاء |
| `Midnight` | نیمه شب شرعی |
| `week` | روز هفته |
| `ys / ms / ds` | تاریخ شمسی |
| `yg / mg / dg` | تاریخ قمری |
| `ym / mm / dm` | تاریخ میلادی |

---

## ⚠️ مدیریت خطاها

| وضعیت | پیام |
|------|------|
| `400` | پارامتر شهر ارسال نشده |
| `404` | شهر مورد نظر یافت نشد |
| `500` | خطای داخلی سرور |

---

### 🧾 نمونه خطا

```json
{
  "status": 404,
  "message": "شهر مورد نظر یافت نشد"
}
```

---

# 💻 استفاده در Python

```py
import requests

API = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=مشهد"

res = requests.get(API, timeout=10)
data = res.json()

print(data["data"]["prayer_times"]["out"]["Maghrib"])
```

---

# 💻 استفاده در Node.js

```js
const API = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=مشهد";

fetch(API)
  .then(res => res.json())
  .then(data => {
    console.log(data.data.prayer_times.out.Fajr);
  })
  .catch(err => console.error(err));
```

---

## 🤖 استفاده در ربات‌ها

✅ ربات‌های مذهبی
✅ ربات اذان‌گو
✅ اپلیکیشن‌های تقویم
✅ وب‌سایت‌های اسلامی
✅ پروژه‌های دانشجویی


---

## ⚙️ ویژگی‌ها

✅ بدون نیاز به API Key
✅ پاسخ سریع
✅ خروجی JSON استاندارد
✅ پشتیبانی از شهرهای ایران
✅ تاریخ شمسی، قمری و میلادی


---

# 👤 Developer

mir sina banihashem / Abolfazl Zarei

🧑‍💻 Developer: @Ninga_code / @Sinabani_api
🌐 API URL: https://abolfazlzarei.sbs/ReligiousTimes.php

---

---

# 🕌 Religious Times API
### Version: Religious Times API v1.0.0

The **Religious Times API** is a fast, lightweight, and API-key-free web service for  
🕋 **fetching Islamic prayer times and location data for Iranian cities**.

By providing a city name, this API returns accurate prayer times along with  
geographical information and **Gregorian, Persian (Shamsi), and Hijri dates** in a  
clean and structured **JSON** response.

🔹 No API Key required  
🔹 Suitable for bots, websites, and mobile applications  
🔹 Includes full prayer times and calendar information  

---

## 🧠 API Architecture

1️⃣ Client sends a request with the city name  
2️⃣ Server resolves the city and its geographical coordinates  
3️⃣ Prayer times are calculated based on location  
4️⃣ Final standardized JSON response is returned  

---

## 🌐 Main API URL

https://abolfazlzarei.sbs/ReligiousTimes.php

---

## 🔗 Endpoint

### 🔹 Get Prayer Times by City

```http
GET /oghat?q={CITY_NAME}
```

---

## 📌 Input Parameters

| Parameter | Type | Description |
|----------|------|-------------|
| `q` | `string` | City name (e.g. Mashhad, Tehran, Qom) |

---

# 🧪 Example Request

GET https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=Mashhad


---

# 📦 API Response Structure

```json
{
  "status": 200,
  "message": "Data retrieved successfully",
  "data": {
    "location": {
      "coordinates": {
        "latitude": "179.87",
        "longitude": "259.2"
      },
      "address_parts": [
        "Mashhad",
        "Razavi Khorasan Province"
      ],
      "city": "Mashhad",
      "province": "Razavi Khorasan Province",
      "full_address": "Mashhad, Razavi Khorasan Province"
    },
    "prayer_times": {
      "status": 200,
      "out": {
        "Fajr": "05:08",
        "Sunrise": "06:35",
        "Dhuhr": "11:45",
        "Asr": "14:33",
        "Sunset": "16:54",
        "Maghrib": "17:14",
        "Isha": "18:03",
        "Midnight": "23:01",
        "FFajr": "05:07",
        "FSunrise": "06:34",
        "ym": 2026,
        "mm": 1,
        "dm": 29,
        "yg": 1447,
        "mg": "Sha'ban",
        "dg": 9,
        "ds": 9,
        "ys": 1404,
        "ms": 11,
        "week": "Thursday",
        "l1": "179.87",
        "l2": "259.2"
      }
    }
  },
  "developer": "@Ninga_code",
  "timestamp": "2026-01-29T09:12:47+00:00"
}
```

---

## 🧾 Important Response Fields

### 📍 Location

| Field | Description |
|------|-------------|
| `latitude` | Latitude |
| `longitude` | Longitude |
| `city` | City name |
| `province` | Province / State |
| `full_address` | Full resolved address |

---

### 🕰 Prayer Times

| Field | Description |
|------|-------------|
| `Fajr` | Fajr prayer time |
| `Sunrise` | Sunrise time |
| `Dhuhr` | Dhuhr prayer time |
| `Asr` | Asr prayer time |
| `Sunset` | Sunset time |
| `Maghrib` | Maghrib prayer time |
| `Isha` | Isha prayer time |
| `Midnight` | Islamic midnight |
| `week` | Day of the week |
| `ys / ms / ds` | Persian (Shamsi) date |
| `yg / mg / dg` | Hijri (Lunar) date |
| `ym / mm / dm` | Gregorian date |

---

## ⚠️ Error Handling

| Status | Message |
|-------|--------|
| `400` | City parameter is missing |
| `404` | City not found |
| `500` | Internal server error |

---

### 🧾 Error Response Example

```json
{
  "status": 404,
  "message": "City not found"
}
```

---

# 💻 Python Example

```py
import requests

API = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=Mashhad"

res = requests.get(API, timeout=10)
data = res.json()

print(data["data"]["prayer_times"]["out"]["Maghrib"])
```

---

# 💻 Node.js Example

```js
const API = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q=Mashhad";

fetch(API)
  .then(res => res.json())
  .then(data => {
    console.log(data.data.prayer_times.out.Fajr);
  })
  .catch(err => console.error(err));
```

---

## ⚙️ Features

✅ No API Key required
✅ Fast and lightweight
✅ Standard JSON response
✅ Supports Iranian cities
✅ Includes Hijri, Persian, and Gregorian dates


---

## 🎯 Use Cases

● Islamic prayer bots
● Azan reminder applications
● Religious websites
● Calendar and timetable apps
● Student and professional projects


---

# 👤 Developer

mir sina banihashem / Abolfazl Zarei

🧑‍💻 Developer: @Ninga_code / @Sinabani_api
🌐 API Endpoint: https://abolfazlzarei.sbs/ReligiousTimes.php
