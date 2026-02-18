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

=========
التطوير
=========

GitHub
------

نطوّر python-snap7 على `GitHub <https://github.com/gijzelaerr/python-snap7>`_.
إذا كان لديك أسئلة حول python-snap7، يُرجى طرح سؤال في
`جلسات النقاش <https://github.com/gijzelaerr/python-snap7/discussions/categories/q-a>`_.
إذا كان لديك بلاغ عن خطأ أو طلب ميزة جديدة، يُرجى رفع مشكلة في
`متتبع المشاكل <https://github.com/gijzelaerr/python-snap7/issues>`_.
الأفضل من ذلك إذا كان لديك حل للمشكلة! في هذه الحالة يمكنك تسهيل عملنا
باتباع هذه الخطوات:

 * قم بعمل fork لمستودعنا على GitHub
 * أضف اختبارات ستفشل بسبب المشكلة
 * أصلح المشكلة
 * شغّل مجموعة الاختبارات مرة أخرى
 * قم بعمل commit في مستودعك
 * أرسل طلب سحب (Pull Request) على GitHub

كما نحاول أن نكون متوافقين قدر الإمكان مع معايير PEP8، حيثما أمكن ذلك ومعقولاً.

مجموعة الاختبارات
------------------

يأتي python-snap7 مع مجموعة اختبارات تغطي ما يقارب 100% من الكود. تتحقق
مجموعة الاختبارات من أن الكود يعمل فعلاً وتجعل التطوير أسهل بكثير.
لتشغيل جميع الاختبارات، شغّل من المصدر::

    $ make test

لاحظ أن بعض الاختبارات تتطلب التشغيل كمستخدم جذر (root)، حيث يحتاج snap7
للربط على منفذ TCP مميز.

إذا اشتكت الاختبارات من وحدات بايثون مفقودة، تأكد أن مجلد المصدر
موجود في متغير البيئة `PYTHONPATH`، أو أن وحدة python-snap7 مثبتة.

Tox
---

لدينا أيضاً مجموعة كاملة من أدوات التحقق من جودة الكود،
يمكنك تشغيلها باستخدام::

    $ make tox

الشكر والتقدير
---------------

تم إنشاء python-snap7 بواسطة:

* `Gijs Molenaar <https://github.com/gijzelaerr>`_
* Stephan Preeker (stephan at preeker dot net)


شكر خاص لـ:

* Davide Nardella لإنشاء snap7
* Thomas Hergenhahn لمكتبة libnodave
* Thomas W لإضافة S7comm في wireshark
* `Fabian Beitler <https://github.com/swamper123>`_
* `Nikteliy <https://github.com/nikteliy>`_
* `Lautaro Nahuel Dapino <https://github.com/lautarodapin>`_
