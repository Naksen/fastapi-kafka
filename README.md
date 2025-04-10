# Kafka Consumer and Producer with FastAPI

## Описание

1. Producer — отправляет сообщения в Kafka topic.

2. Consumer — получает сообщения из Kafka topic и обрабатывает их.

## Установка и запуск

1. Создать `.env` файл в корне проекта по аналогии с `env-example`.
2. Поместить в `./consumer/certs` и `./producer/certs` сертификат `cert.pem`.
3. Запустить `docker compose up`.

## Проверка работы

1. http://localhost:8000/send - отправить сообщение в Kafka.
2. http://localhost:8001/messages - получить последние 10 сообщений из топика.
