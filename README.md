# HRMS – Human Resource Management System

A full-stack Human Resource Management System (HRMS) built using Django REST Framework and React. This project is production-ready, fully deployed, and documented using Swagger (OpenAPI).

---

## 🚀 Live Demo

* **Frontend:** [https://frontend-hrms-omega.vercel.app/](https://frontend-hrms-omega.vercel.app/)
* **Backend (Swagger API):** [https://backend-hrms-umwx.onrender.com/swagger-ui/](https://backend-hrms-umwx.onrender.com/swagger-ui/)

---

## 📂 Source Code

* **Frontend GitHub:** [https://github.com/sohailk007/frontend-hrms](https://github.com/sohailk007/frontend-hrms)
* **Backend GitHub:** [https://github.com/sohailk007/backend-hrms](https://github.com/sohailk007/backend-hrms)

---

## 🛠 Tech Stack

### Backend

* Django
* Django REST Framework (DRF)
* PostgreSQL
* drf-spectacular (Swagger / OpenAPI)

### Frontend

* React (Vite)
* Axios
* Tailwind CSS (if used)

### Deployment

* Backend: Render
* Frontend: Vercel

---

## ✨ Features

* Employee management (Create, Read, Update, Delete)
* Attendance marking and tracking
* Attendance summaries per employee
* Dashboard analytics (total employees, attendance records, present count)
* RESTful APIs with full Swagger documentation
* Environment-based configuration using `.env`

---

## 🔗 API Endpoints Overview

### Employee

* `GET /api/v1/employees/` – List employees
* `POST /api/v1/employees/` – Create employee
* `DELETE /api/v1/employees/{id}/` – Delete employee

### Attendance

* `POST /api/v1/attendance/create/` – Mark attendance
* `GET /api/v1/attendance/list/` – List attendance records (filter by employee_id, date)

### Summary

* `GET /api/v1/attendance/summary/` – Attendance summary per employee
* `GET /api/v1/dashboard/summary/` – Dashboard statistics

(For full API details, refer to Swagger UI.)

---

## ⚙️ Backend Setup

```bash
git clone https://github.com/sohailk007/backend-hrms.git
cd backend-hrms
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Create a `.env` file:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/hrms_db
```

---

## ⚙️ Frontend Setup

```bash
git clone https://github.com/sohailk007/frontend-hrms.git
cd frontend-hrms
npm install
npm run dev
```

Create a `.env` file:

```env
VITE_BASE_URL=http://localhost:8000/api/v1
```

---

## 📄 Documentation

Swagger API documentation is available at:

👉 [https://backend-hrms-umwx.onrender.com/swagger-ui/](https://backend-hrms-umwx.onrender.com/swagger-ui/)

---

## 🧪 Testing

* APIs can be tested directly via Swagger UI.
* Frontend uses Axios for API communication.

---

## 📈 Future Enhancements

* User authentication & role-based access control
* Pagination, filtering, and search
* Export reports (PDF/Excel)
* Notification system
* Audit logs

---

## 👤 Author

Md Sohail Ali
Full Stack Python Developer
GitHub: [https://github.com/sohailk007](https://github.com/sohailk007)
LinkedIn: [https://linkedin.com/in/md-sohail](https://linkedin.com/in/md-sohail)

---

## 📜 License

This project is open-source and available under the MIT License.
