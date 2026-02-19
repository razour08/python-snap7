.. raw:: html

   <style>
   .arabic-doc, .arabic-doc * {
       direction: rtl;
       text-align: right;
   }
   .arabic-doc code, .arabic-doc pre, .arabic-doc .highlight {
       direction: ltr;
       text-align: left;
   }
   </style>

.. rst-class:: arabic-doc

استكشاف الأخطاء وإصلاحها
===========================


مكتبة snap7 غير موجودة
-----------------------

**الخطأ**: ``can't find snap7 shared library``

**السبب**: مكتبة snap7 الأصلية غير مثبتة أو غير موجودة في مسار النظام.

**الحل**:

1. التثبيت عبر pip (موصى به)::

      $ pip install python-snap7

2. أو تثبيت المكتبة الأصلية يدوياً:

   - **أوبونتو**: ``sudo apt install libsnap7-1``
   - **ماك**: ``brew install snap7``
   - **ويندوز**: التنزيل من SourceForge ووضع ``snap7.dll`` في مسار النظام


رفض الاتصال
------------

**الخطأ**: ``errIsoConnect`` أو انتهاء مهلة الاتصال

**الأسباب المحتملة**:

1. عنوان IP أو رقم الراك أو الفتحة غير صحيح
2. PLC غير قابل للوصول على الشبكة
3. اتصال PUT/GET غير مفعّل (S7-1200/1500)
4. جدار الحماية يحجب المنفذ 102

**الحلول**:

1. تحقق من عنوان IP الخاص بـ PLC: ``ping 192.168.0.1``
2. تحقق من الراك/الفتحة (انظر الأسئلة الشائعة)
3. فعّل PUT/GET في TIA Portal (انظر الأسئلة الشائعة)
4. افتح المنفذ 102 في جدار الحماية


خطأ حجم PDU
------------

**الخطأ**: ``errCliSizeOverPDU``

**السبب**: محاولة قراءة/كتابة بيانات أكبر مما يسمح به PDU.

**الحل**: قسّم القراءات الكبيرة إلى أجزاء أصغر:

.. code-block:: python

    # بدلاً من قراءة 1000 بايت دفعة واحدة:
    # data = client.db_read(1, 0, 1000)  # قد يفشل!

    # اقرأ على أجزاء:
    chunk_size = 200
    data = bytearray()
    for offset in range(0, 1000, chunk_size):
        size = min(chunk_size, 1000 - offset)
        data += client.db_read(1, offset, size)


تم رفض الإذن
--------------

**الخطأ**: ``errCliNeedPassword`` أو ``errCliFunctionRefused``

**السبب**: يتطلب PLC كلمة مرور أو الوظيفة محظورة.

**الحل**:

1. اضبط كلمة مرور PLC:

   .. code-block:: python

       client.set_session_password("your_password")

2. تحقق من مستوى الحماية في TIA Portal


عنوان غير صالح
----------------

**الخطأ**: ``errCliAddressOutOfRange``

**السبب**: رقم DB أو عنوان البداية أو الحجم غير صالح.

**الحل**:

1. تحقق من وجود DB على PLC
2. تحقق من حجم DB في مشروع PLC
3. تأكد أن ``start + size`` لا يتجاوز طول DB


خطأ بدء الخادم
-----------------

**الخطأ**: ``errSrvCannotStart`` عند تشغيل خادم S7

**السبب**: المنفذ 102 مستخدم بالفعل أو يتطلب صلاحيات مرتفعة.

**الحلول**:

1. شغّل كمسؤول/جذر (root)
2. أوقف أي خوادم snap7 موجودة
3. تحقق مما إذا كان منفذ 102 مستخدماً من عملية أخرى::

      # لينكس/ماك
      $ lsof -i :102

      # ويندوز
      > netstat -ano | findstr :102
