# 🚀 Deployment Guide - Stroke Prediction Web App

Your application is ready to deploy! Follow the steps below for your preferred platform.

---

## 📋 **Prerequisites**

- ✅ GitHub account (already have)
- ✅ Code pushed to repository
- ✅ All requirements.txt dependencies listed
- ✅ Environment variables configured

---

## 🟢 **OPTION 1: RENDER.COM (RECOMMENDED - FREE)**

### Best for: Quick deployment, minimal setup

**Step 1: Create Account**
- Go to https://render.com
- Sign up with GitHub

**Step 2: Connect Repository**
1. Click "New +" → "Web Service"
2. Select "Build and deploy from GitHub"
3. Search for `Stroke-Prediction` repository
4. Click "Connect"

**Step 3: Configure Service**
- **Name**: `stroke-prediction-app`
- **Environment**: Python 3
- **Region**: Choose closest to you
- **Branch**: `main`
- **Build Command**: 
  ```
  pip install -r requirements.txt && cd prediction && python manage.py migrate && python manage.py collectstatic --noinput
  ```
- **Start Command**: 
  ```
  cd prediction && gunicorn prediction.wsgi:application --bind 0.0.0.0:$PORT
  ```

**Step 4: Add Environment Variables**
Click "Advanced" and add:
```
DEBUG = False
SECRET_KEY = render-secret-key-2024
ALLOWED_HOSTS = your-app.onrender.com
DATABASE_URL = sqlite:///db.sqlite3
```

**Step 5: Deploy**
- Click "Create Web Service"
- Wait 5-10 minutes for deployment
- Your URL: `https://your-app-name.onrender.com`

---

## 🔵 **OPTION 2: HEROKU**

### Best for: Scalable apps, production use

**Step 1: Install Heroku CLI**
```bash
# macOS
brew install heroku

# Windows (using npm)
npm install -g heroku
```

**Step 2: Login to Heroku**
```bash
heroku login
```

**Step 3: Create App**
```bash
heroku create stroke-prediction-app
```

**Step 4: Set Environment Variables**
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set ALLOWED_HOSTS="stroke-prediction-app.herokuapp.com"
```

**Step 5: Deploy**
```bash
git push heroku main
```

**Step 6: Run Migrations**
```bash
heroku run python prediction/manage.py migrate
```

**Your URL**: `https://stroke-prediction-app.herokuapp.com`

---

## 🟣 **OPTION 3: RAILWAY.APP**

### Best for: Modern, easy deployment

**Step 1: Go to Railway**
- Visit https://railway.app
- Sign up with GitHub

**Step 2: Create New Project**
- Click "Create New Project"
- Select "Deploy from GitHub"
- Choose repository

**Step 3: Configure**
- Railway auto-detects Django
- Add environment variables in "Variables" tab

**Step 4: Deploy**
- Click "Deploy"
- Get your URL from "Domains" section

---

## 🟠 **OPTION 4: PYTHONANYWHERE**

### Best for: Python-focused hosting

1. Go to https://www.pythonanywhere.com
2. Create free account
3. Upload code via Git
4. Configure WSGI file
5. Enable website

---

## 🟡 **OPTION 5: AWS (ELASTIC BEANSTALK)**

### Best for: Production, heavy traffic

```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 stroke-prediction

# Create environment
eb create stroke-app

# Deploy
eb deploy
```

---

## ⚙️ **Environment Variables Setup**

Create `.env` file in root directory:

```env
# Django Settings
DEBUG=False
SECRET_KEY=your-super-secret-key
ALLOWED_HOSTS=your-domain.com,localhost

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=stroke_db
DB_USER=postgres
DB_PASSWORD=secure-password
DB_HOST=localhost
DB_PORT=5432

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## 🔧 **Local Testing Before Deployment**

```bash
# Navigate to project
cd prediction

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver 0.0.0.0:8000
```

Visit: `http://localhost:8000`

---

## ✅ **Post-Deployment Checklist**

- [ ] Website loads without errors
- [ ] Login/signup works
- [ ] Stroke prediction form submits
- [ ] Appointments can be booked
- [ ] Static files load (CSS, images)
- [ ] Database is working
- [ ] Error handling works
- [ ] HTTPS is enabled

---

## 🐛 **Troubleshooting**

### "Module not found" Error
```bash
# Reinstall requirements
pip install -r requirements.txt
```

### Database Errors
```bash
# Run migrations
python manage.py migrate
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput
```

### Model Not Loading
- Ensure `my_stroke_model.pkl` is in `prediction/` folder
- Check file permissions

---

## 📊 **Monitoring & Maintenance**

### View Logs
- **Render**: Dashboard → Logs tab
- **Heroku**: `heroku logs --tail`
- **Railway**: Dashboard → Logs

### Update Code
```bash
git add .
git commit -m "Update features"
git push origin main
git push heroku main  # For Heroku
```

---

## 🎯 **Your Live Demo URLs**

After deployment, share these links:
- **Production**: `https://your-app-name.onrender.com`
- **Admin Panel**: `https://your-app-name.onrender.com/admin`
- **API**: `https://your-app-name.onrender.com/api/predict/`

---

## 📞 **Need Help?**

- Check platform-specific docs
- Review error logs
- Test locally first
- Contact platform support

---

## 🎉 **Congratulations!**

Your Stroke Prediction app is now live and accessible to everyone! 🚀
