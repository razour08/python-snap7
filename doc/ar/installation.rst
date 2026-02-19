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

التثبيت عبر الحزمة الثنائية
============================

ننصحك بتثبيت python-snap7 باستخدام الحزمة الثنائية (binary wheel).
يجب أن تعمل الحزم الثنائية على ويندوز 64 بت، وماك (Intel)،
ولينكس x64 ولينكس ARM.

python-snap7 متاح على `PyPI <https://pypi.python.org/pypi/python-snap7/>`_.
يمكنك تثبيته باستخدام pip::

  $ pip install python-snap7

إذا كنت تريد استخدام واجهة سطر الأوامر لتشغيل محاكي، يجب تثبيتها مع::

  $ pip install "python-snap7[cli]"


التثبيت اليدوي (غير مُوصَى به)
================================

إذا كنت تستخدم منصة غير مدعومة، ستحتاج إلى بعض العمل الإضافي.
يتضمن ذلك خطوتين: أولاً، تثبيت مكتبة snap7،
ثم تثبيت حزمة python-snap7.

مكتبة Snap7
-----------

أوبونتو
~~~~~~~~

إذا كنت تستخدم أوبونتو، يمكنك استخدام حزم أوبونتو من
`PPA الخاص بنا على لانشباد <https://launchpad.net/~gijzelaar/+archive/snap7>`_.
للتثبيت::

    $ sudo add-apt-repository ppa:gijzelaar/snap7
    $ sudo apt-get update
    $ sudo apt-get install libsnap7-1 libsnap7-dev

ويندوز
~~~~~~~

قم بتنزيل ملف zip من
`صفحة SourceForge <https://sourceforge.net/projects/snap7/files/>`_.
فك ضغط الملف، وانسخ ``release\\Windows\\Win64\\snap7.dll`` إلى مكان
في مسار النظام (PATH)، على سبيل المثال ``%systemroot%\System32\``.
أو يمكنك نسخ الملف إلى مكان آخر وتعديل مسار النظام.

ماك (macOS)
~~~~~~~~~~~

مكتبة snap7 متاحة على `Homebrew <https://brew.sh/>`_::

  $ brew install snap7


التجميع من المصدر
~~~~~~~~~~~~~~~~~~

قم بتنزيل أحدث مصدر من
`صفحة SourceForge <https://sourceforge.net/projects/snap7/files/>`_
وقم بالتجميع يدوياً. قم بتنزيل الملف وشغّل::

     $ p7zip -d snap7-full-1.0.0.7z  # يتطلب برنامج p7zip
     $ cd build/<platform>           # حيث platform هي unix أو windows
     $ make -f <arch>.mk install     # حيث arch هي معمارية النظام، مثلاً x86_64_linux

لمزيد من المعلومات أو المساعدة في التجميع، يُرجى مراجعة التوثيق على
`موقع snap7 <https://snap7.sourceforge.net/>`_.


تثبيت Python-Snap7
-------------------

بعد توفر snap7 في مسار المكتبات أو مسار النظام، يمكنك تثبيتها من
مستودع git أو من ملف المصدر المضغوط. يُنصح بتثبيتها في بيئة افتراضية.

لإنشاء بيئة افتراضية وتفعيلها::

  $ python3 -m venv venv
  $ source venv/bin/activate

الآن يمكنك تثبيت حزمة python-snap7::

  $ pip3 install .
