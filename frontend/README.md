# Flutter Project – Getting Started Guide

Welcome to the project 👋 This guide will help you and your collaborators quickly set up and run the Flutter app locally.

---

## 📦 Prerequisites

Before you start, make sure you have the following installed:

### 1. Flutter SDK

* Install Flutter: [https://docs.flutter.dev/get-started/install](https://docs.flutter.dev/get-started/install)
* Verify installation:

```bash
flutter doctor
```

### 2. Dart (included with Flutter)

No separate install needed if Flutter is installed correctly.

### 3. Git

* Install Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)

### 4. IDE (recommended)

* VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

  * Install Flutter + Dart extensions
* OR Android Studio: [https://developer.android.com/studio](https://developer.android.com/studio)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Get dependencies

```bash
flutter pub get
```

### 3. Run the app

#### For Android / iOS emulator or physical device:

```bash
flutter run
```

#### For web (if enabled):

```bash
flutter run -d chrome
```

---

## 🧪 Useful Flutter Commands

### Check environment setup

```bash
flutter doctor
```

### Clean build cache

```bash
flutter clean
flutter pub get
```

### Run tests

```bash
flutter test
```

### Analyze code

```bash
flutter analyze
```

---

## 📁 Project Structure (typical)

```
lib/
  main.dart           # App entry point
  screens/            # UI screens
  widgets/            # Reusable components
  services/           # API / backend logic
  models/             # Data models
```

---

## 🌿 Git Workflow

We use a feature-branch + PR workflow:

### Create a new branch

```bash
git checkout -b feature/your-feature-name
```

### Push your branch

```bash
git push origin feature/your-feature-name
```

### Then:

* Open a Pull Request on GitHub
* Request review
* Merge after approval

⚠️ Direct pushes to `main` are not allowed.

---

## ⚙️ Environment Notes

If your app uses environment variables or API keys:

* Create a `.env` file (if applicable)
* Do NOT commit secrets to GitHub

---

## 🛠 Troubleshooting

### Flutter not found

Make sure Flutter is in your PATH:

```bash
export PATH="$PATH:/path-to-flutter/bin"
```

### Dependency issues

```bash
flutter pub cache repair
flutter pub get
```

### iOS build issues (Mac only)

```bash
cd ios
pod install
```

---

## 📌 Recommended First Steps for New Contributors

1. Run `flutter doctor`
2. Clone repo
3. Run `flutter pub get`
4. Launch app with `flutter run`
5. Create a test feature branch

---

## 🤝 Contributing

1. Fork or branch from `master`
2. Make changes
3. Run tests + analyze code
4. Submit a PR

---

Happy coding 🚀
