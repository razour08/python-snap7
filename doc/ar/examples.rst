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

أمثلة عملية
============

فيما يلي أمثلة عملية شائعة للعمل مع أجهزة PLC من سيمنز.


مثال 1: قراءة بيانات المستشعرات
---------------------------------

قراءة قيم مستشعرات درجة الحرارة والضغط من كتلة بيانات:

.. code-block:: python

    import snap7
    from snap7.util import get_real, get_int

    # الاتصال بـ PLC
    client = snap7.Client()
    client.connect("192.168.0.1", 0, 0)

    # قراءة كتلة البيانات رقم 1 (20 بايت ابتداءً من العنوان 0)
    data = client.db_read(1, 0, 20)

    # استخراج القيم
    temperature = get_real(data, 0)     # درجة الحرارة (REAL) عند البايت 0
    pressure = get_real(data, 4)        # الضغط (REAL) عند البايت 4
    sensor_id = get_int(data, 8)        # رقم المستشعر (INT) عند البايت 8

    print(f"درجة الحرارة: {temperature:.1f} °C")
    print(f"الضغط: {pressure:.2f} بار")
    print(f"رقم المستشعر: {sensor_id}")

    client.disconnect()


مثال 2: كتابة أوامر التحكم
-----------------------------

إرسال أوامر التحكم إلى PLC لتشغيل/إيقاف محرك:

.. code-block:: python

    import snap7
    from snap7.util import set_bool

    client = snap7.Client()
    client.connect("192.168.0.1", 0, 0)

    # قراءة البايت الحالي من كتلة البيانات
    data = client.db_read(2, 0, 1)

    # تشغيل المحرك (البت 0 من البايت 0)
    set_bool(data, 0, 0, True)
    client.db_write(2, 0, data)
    print("✅ تم تشغيل المحرك")

    # إيقاف المحرك
    set_bool(data, 0, 0, False)
    client.db_write(2, 0, data)
    print("⛔ تم إيقاف المحرك")

    client.disconnect()


مثال 3: مراقبة حالة PLC
--------------------------

فحص حالة وحدة المعالجة المركزية ومعلومات النظام:

.. code-block:: python

    import snap7

    client = snap7.Client()
    client.connect("192.168.0.1", 0, 0)

    # حالة وحدة المعالجة
    state = client.get_cpu_state()
    print(f"حالة المعالج: {state}")

    # معلومات وحدة المعالجة
    info = client.get_cpu_info()
    print(f"نوع الوحدة: {info.ModuleTypeName}")
    print(f"الرقم التسلسلي: {info.SerialNumber}")

    # معلومات الاتصال
    connected = client.get_connected()
    print(f"متصل: {'نعم' if connected else 'لا'}")

    client.disconnect()


مثال 4: استخدام المحاكي للاختبار
-----------------------------------

تشغيل خادم S7 محلي للاختبار بدون PLC حقيقي:

.. code-block:: python

    import snap7
    import ctypes

    # إنشاء وتشغيل الخادم
    server = snap7.Server()

    # تسجيل منطقة ذاكرة
    db_data = (ctypes.c_ubyte * 256)()
    server.register_area(snap7.SrvArea.DB, 1, db_data)

    # بدء الخادم
    server.start()
    print("🖥️ الخادم يعمل على المنفذ 102")

    # الآن يمكنك الاتصال بالخادم من عميل آخر
    client = snap7.Client()
    client.connect("127.0.0.1", 0, 0)

    # كتابة بيانات
    client.db_write(1, 0, bytearray([0x01, 0x02, 0x03]))

    # قراءة البيانات
    result = client.db_read(1, 0, 3)
    print(f"البيانات: {list(result)}")

    client.disconnect()
    server.stop()


مثال 5: قراءة متعددة (Multi-Read)
-------------------------------------

قراءة عدة مناطق بيانات في طلب واحد لتحسين الأداء:

.. code-block:: python

    import snap7
    from snap7.type import Area, WordLen, S7DataItem
    import ctypes

    client = snap7.Client()
    client.connect("192.168.0.1", 0, 0)

    # تحضير عناصر القراءة
    items = []

    # العنصر 1: قراءة من DB1
    item1 = S7DataItem()
    item1.Area = Area.DB
    item1.WordLen = WordLen.Byte
    item1.DBNumber = 1
    item1.Start = 0
    item1.Amount = 10
    buffer1 = (ctypes.c_uint8 * 10)()
    item1.pData = ctypes.cast(buffer1, ctypes.POINTER(ctypes.c_uint8))
    items.append(item1)

    # العنصر 2: قراءة من DB2
    item2 = S7DataItem()
    item2.Area = Area.DB
    item2.WordLen = WordLen.Byte
    item2.DBNumber = 2
    item2.Start = 0
    item2.Amount = 20
    buffer2 = (ctypes.c_uint8 * 20)()
    item2.pData = ctypes.cast(buffer2, ctypes.POINTER(ctypes.c_uint8))
    items.append(item2)

    # تنفيذ القراءة المتعددة
    result = client.read_multi_vars(items)

    print(f"DB1: {bytearray(buffer1)}")
    print(f"DB2: {bytearray(buffer2)}")

    client.disconnect()
