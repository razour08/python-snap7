FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

LABEL org.opencontainers.image.source=https://github.com/gijzelaerr/python-snap7
LABEL org.opencontainers.image.description="Python wrapper for the Snap7 PLC communication library"
LABEL org.opencontainers.image.licenses=MIT

# Install system dependencies and snap7 library
# تثبيت متطلبات النظام ومكتبة snap7
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    software-properties-common \
    python3-pip \
    python3-venv \
    && add-apt-repository ppa:gijzelaar/snap7 \
    && apt-get update \
    && apt-get install -y --no-install-recommends libsnap7-dev libsnap7-1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment / إنشاء بيئة افتراضية
WORKDIR /venv
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install python-snap7 / تثبيت python-snap7
ADD . /code
RUN pip install --no-cache-dir /code[cli]

# Expose S7 default port / كشف منفذ S7 الافتراضي
EXPOSE 102

# Default: run the S7 server emulator
# الافتراضي: تشغيل محاكي خادم S7
CMD ["snap7-server"]
