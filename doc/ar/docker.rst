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

Docker (حاويات دوكر)
=====================

يوفر python-snap7 دعم Docker لتشغيل محاكي خادم S7 ولأغراض التطوير.


بناء صورة Docker
-----------------

بناء الصورة::

    $ docker build -t python-snap7 .

تشغيل الحاوية::

    $ docker run -p 102:102 python-snap7 snap7-server

سيبدأ هذا محاكي خادم S7 يستمع على المنفذ 102، وهو منفذ اتصال S7 القياسي.


Docker Compose
--------------

يتوفر ملف ``docker-compose.yml`` يحتوي على خدمتين:

**snap7-server** — محاكي خادم S7
    يبدأ محاكي خادم snap7 المدمج لاختبار اتصال PLC.
    يعرض المنفذ 102 لاتصالات عميل S7.

**snap7-dev** — بيئة التطوير
    يربط الكود المصدري في الحاوية للتطوير المباشر والاختبار.
    يُفعّل بملف التعريف ``dev``.

تشغيل محاكي الخادم::

    $ docker-compose up

التشغيل في الخلفية::

    $ docker-compose up -d

إيقاف وحذف الحاويات::

    $ docker-compose down

تشغيل بيئة التطوير::

    $ docker-compose --profile dev run snap7-dev

فتح سطر أوامر في حاوية التطوير::

    $ docker-compose --profile dev run snap7-dev bash


الاتصال بالمحاكي
-----------------

بعد تشغيل الخادم، يمكنك الاتصال من جهازك:

.. code-block:: python

    import snap7

    client = snap7.Client()
    client.connect("127.0.0.1", 0, 0, 102)

    # التحقق من الاتصال
    print(f"متصل: {client.get_connected()}")

    # قراءة معلومات وحدة المعالجة
    cpu_info = client.get_cpu_info()
    print(f"المعالج: {cpu_info}")

    client.disconnect()


مرجع Dockerfile
-----------------

ملف ``Dockerfile`` المرفق مبني على Ubuntu 24.04 ويقوم بـ:

1. تثبيت مكتبة snap7 الأصلية من مستودع PPA
2. إنشاء بيئة بايثون افتراضية
3. تثبيت python-snap7 في البيئة الافتراضية

أمر ``snap7-server`` في واجهة سطر الأوامر متاح بعد البناء،
ويقوم بتشغيل محاكي خادم S7 أساسي.
