حول المشروع
============

.. image:: https://img.shields.io/pypi/v/python-snap7.svg
   :target: https://pypi.python.org/pypi/python-snap7/

.. image:: https://img.shields.io/pypi/pyversions/python-snap7.svg
   :target: https://pypi.python.org/pypi/python-snap7/

.. image:: https://img.shields.io/github/license/gijzelaerr/python-snap7.svg
   :target: https://github.com/gijzelaerr/python-snap7/blob/master/LICENSE

.. image:: https://img.shields.io/github/actions/workflow/status/gijzelaerr/python-snap7/testing.yml?label=tests
   :target: https://github.com/gijzelaerr/python-snap7/actions

.. raw:: html

   <p align="center">
     <strong>🌍 Language / اللغة:</strong>&nbsp;&nbsp;
     <a href="README.rst">English</a> |
     <a href="README_AR.rst"><strong>العربية</strong></a>
   </p>

هذا مُغلّف بايثون لمكتبة `Snap7 <https://snap7.sourceforge.net>`_، وهي مكتبة مفتوحة المصدر
للاتصال عبر الإيثرنت (32/64 بت، متعددة المنصات) للتواصل المباشر مع وحدات التحكم المنطقية
القابلة للبرمجة (PLC) من سيمنز طراز S7.

تم اختبار python-snap7 مع بايثون 3.10 وما فوق، على أنظمة ويندوز ولينكس وماك.

التوثيق الكامل متاح على `Read The Docs <https://python-snap7.readthedocs.io/en/latest/>`_.


الميزات الرئيسية
=================

* 📡 **الاتصال بـ PLC** — قراءة وكتابة كتل البيانات والمدخلات والمخرجات ومناطق الذاكرة
* 🔄 **التحكم بـ PLC** — تشغيل وإيقاف وإعادة تشغيل PLC عن بعد
* 📊 **التشخيص** — قراءة معلومات وحدة المعالجة المركزية وحالتها
* 🖥️ **خادم S7** — محاكي خادم S7 مدمج للاختبار
* 🤝 **الشركاء** — اتصال نظير لنظير بين أجهزة PLC
* 🏗️ **دعم Logo** — الاتصال بأجهزة Siemens Logo PLC
* 🛠️ **أدوات مساعدة** — دوال تحويل البيانات لأنواع البيانات الصناعية


التثبيت
=======

إذا كنت تستخدم ويندوز (amd64) أو ماك (amd64/aarch64) أو جنو/لينكس (amd64/arm64)
أو منصة متوافقة، يمكنك تثبيت الحزمة الثنائية باستخدام::

   $ pip install python-snap7

لاستخدام واجهة سطر الأوامر لتشغيل المحاكي::

   $ pip install "python-snap7[cli]"

وإلا، يُرجى اتباع `تعليمات التثبيت اليدوي <https://python-snap7.readthedocs.io/en/latest/installation.html>`_
لتثبيت python-snap7 من المصدر.


البدء السريع
=============

.. code-block:: python

    import snap7

    # الاتصال بـ PLC
    client = snap7.Client()
    client.connect("192.168.0.1", 0, 0)

    # قراءة كتلة بيانات
    data = client.db_read(1, 0, 10)
    print(f"البيانات: {data}")

    # قطع الاتصال
    client.disconnect()


Docker (حاوية دوكر)
====================

التشغيل باستخدام Docker::

   $ docker build -t python-snap7 .

أو باستخدام Docker Compose::

   $ docker-compose up

راجع `توثيق Docker <doc/ar/docker.rst>`_ لمزيد من التفاصيل.


المساهمة
=========

نرحب بمساهماتكم! يمكنكم المشاركة عبر:

* الإبلاغ عن الأخطاء في `متتبع المشاكل <https://github.com/gijzelaerr/python-snap7/issues>`_
* طرح الأسئلة في `جلسات النقاش <https://github.com/gijzelaerr/python-snap7/discussions/categories/q-a>`_
* تقديم طلبات السحب (Pull Requests) لإصلاح المشاكل أو إضافة ميزات جديدة


الترخيص
========

هذا المشروع مرخّص بموجب `رخصة MIT <LICENSE>`_.
