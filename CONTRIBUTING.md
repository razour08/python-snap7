# Contributing to python-snap7 / المساهمة في python-snap7

<p align="center">
  <strong>🌍 Language / اللغة:</strong>&nbsp;&nbsp;
  <a href="#english"><strong>English</strong></a> |
  <a href="#العربية">العربية</a>
</p>

---

## English

### How to Contribute

We welcome contributions! Here's how you can help:

#### 🐛 Reporting Bugs

1. Check the [existing issues](https://github.com/gijzelaerr/python-snap7/issues) first
2. Create a new issue with:
   - A clear, descriptive title
   - Steps to reproduce the bug
   - Expected vs actual behavior
   - Your environment (OS, Python version, snap7 version)

#### 💡 Feature Requests

1. Open an issue describing the feature you'd like
2. Explain why it would be useful
3. Include code examples if possible

#### 🔧 Pull Requests

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Write tests** that verify your changes
4. **Run** the test suite:
   ```bash
   make test
   ```
5. **Check** code quality:
   ```bash
   make check
   make mypy
   ```
6. **Commit** with clear messages: `git commit -m "Add: description of change"`
7. **Push** to your fork: `git push origin feature/my-feature`
8. **Submit** a Pull Request

#### 📝 Code Style

- Follow PEP 8 guidelines
- Use type annotations for all functions
- Maximum line length: 130 characters
- Run `ruff format` before committing
- Add docstrings in Google style

#### 🧪 Testing

```bash
# Run all tests
make test

# Run specific test
pytest tests/test_client.py

# Run with coverage
pytest --cov=snap7 tests/

# Type checking
make mypy

# Full quality check
make tox
```

#### 📖 Documentation

- Update docstrings when changing function signatures
- Update RST docs if adding new features
- Provide examples in both English and Arabic when possible

---

## العربية

### كيف تساهم

نرحب بمساهماتكم! إليك كيف يمكنك المساعدة:

#### 🐛 الإبلاغ عن الأخطاء

1. تحقق من [المشاكل المفتوحة](https://github.com/gijzelaerr/python-snap7/issues) أولاً
2. أنشئ مشكلة جديدة مع:
   - عنوان واضح ووصفي
   - خطوات إعادة إنتاج الخطأ
   - السلوك المتوقع مقابل الفعلي
   - بيئتك (نظام التشغيل، إصدار بايثون، إصدار snap7)

#### 💡 طلب ميزات جديدة

1. افتح مشكلة تصف الميزة التي تريدها
2. اشرح لماذا ستكون مفيدة
3. أضف أمثلة كود إن أمكن

#### 🔧 طلبات السحب (Pull Requests)

1. **انسخ** المستودع (Fork)
2. **أنشئ** فرع ميزة: `git checkout -b feature/my-feature`
3. **اكتب اختبارات** تتحقق من تغييراتك
4. **شغّل** مجموعة الاختبارات:
   ```bash
   make test
   ```
5. **تحقق** من جودة الكود:
   ```bash
   make check
   make mypy
   ```
6. **سجّل التغييرات** برسائل واضحة: `git commit -m "إضافة: وصف التغيير"`
7. **ادفع** إلى نسختك: `git push origin feature/my-feature`
8. **قدّم** طلب سحب (Pull Request)

#### 📝 أسلوب الكود

- اتبع إرشادات PEP 8
- استخدم التعليقات التوضيحية للأنواع (type annotations) لجميع الدوال
- الطول الأقصى للسطر: 130 حرفاً
- شغّل `ruff format` قبل تسجيل التغييرات
- أضف docstrings بأسلوب Google

#### 🧪 الاختبار

```bash
# تشغيل جميع الاختبارات
make test

# تشغيل اختبار محدد
pytest tests/test_client.py

# تشغيل مع تقرير التغطية
pytest --cov=snap7 tests/

# فحص الأنواع
make mypy

# فحص الجودة الكامل
make tox
```

#### 📖 التوثيق

- حدّث docstrings عند تغيير توقيعات الدوال
- حدّث ملفات RST عند إضافة ميزات جديدة
- قدّم أمثلة بالعربية والإنجليزية عند الإمكان
