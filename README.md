# API DOCUMENTATION

### 1. **Send Otp**

**URL:** `POST /send-otp`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/send-otp](https://budayakita-be-592544960467.asia-southeast2.run.app/send-otp)  
**Request:**

```json
{
    "email": string,
    "full_name": string,
    "password": string
}
```

**Response:**

```json
{
  "message": "OTP telah dikirim ke email"
}
```

---

### 2. **Verify Otp**

**URL:** `POST /verify-otp`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/verify-otp](https://budayakita-be-592544960467.asia-southeast2.run.app/verify-otp)  
**Request:**

```json
{
    "email": string,
    "otp": stirng
}
```

**Response:**

```json
{
  "message": "Akun berhasil dibuat"
}
```

### 3. **login**

**URL:** `POST /login`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/login](https://budayakita-be-592544960467.asia-southeast2.run.app/login)  
**Request:**

```json
{
  tidak ada parameter yang diperlukan
}
```

**Response:**

```json
{
  "results": [
    {
      "label": strign,
      "description": string,
      "image_url": string
    },
    {
      "label": strign,
      "description": string,
      "image_url": string
    }
  ]
}
```

### 4. **Get All Budaya**

**URL:** `GET /getall_budaya`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/getall_budaya](https://budayakita-be-592544960467.asia-southeast2.run.app/getall_budaya)  
**Request:**

```json
{
    "name": string
}
```

**Response:**

```json
{
    "results": [
        {
            "label": string,
            "description": string,
            "image_url": string
        }
        {
            "label": string,
            "description": string,
            "image_url": string
        }
    ]
}
```

### 5. **details**

**URL:** `GET /details`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/details?file_name=[file_name]](https://budayakita-be-592544960467.asia-southeast2.run.app/details?file_name=[file_name])  
**Request:**

```json
{
    "file_name": string,
}
```

**Response:**

```json
{
    "description": string,
    "image_url": string,
    "label": string
}
```

# API DOCUMENTATION

### 6. **Image Prediction**

**URL:** `POST /predict-image`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/predict-image](https://budayakita-be-592544960467.asia-southeast2.run.app/predict-image)  
**Request:**

```json
{
  "file": file,
  "user_id": string
}
```

**Response:**

```json
{
  "confidence": float,
    "created_at": datetime,
    "deskripsi": string,
    "file_url": string,
    "prediction": string,
    "user_id": string
}
```

---

### 7. **Prediction History**

**URL:** `GET /prediction-history?user_id=[user_id]`  
**Endpoint:** [https://budayakita-be-592544960467.asia-southeast2.run.app/prediction-history?user_id=[user_id]](https://prediksi-budaya-592544960467.asia-southeast2.run.app/prediction-history?user_id=0)  
**Request:**

```json
{
  "user_id": string,
}
```

**Response:**

```json
{
    "history": [
        {
            "created_at": datetime,
            "deskripsi": string,
            "file_url": string,
            "filename": string,
            "label_name": string,
            "user_id": string
        },
    ]
}
```

---

---
