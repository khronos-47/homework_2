Сам проект находится  в database\postgresql-docker-image\cart_validation_service .
он запускается в порте localhost:7432 (извините ! в моем компьютере при подключение на порт 80 дает permission denied  и я не смог настроить ) 
Структура проекта:



cart_validation_service/
│
├── app.py
├── validation_strategies/
│   ├── __init__.py
│   ├── common_item_validation.py
│   ├── prescription_item_validation.py
│   ├── special_item_validation.py
│   ├── validation_factory.py
├── database
│   ├── database.py
│   ├── models
│        ├── __init__.py
│        ├── base_model.py
├── search_user
│   ├── serach_factory.py
│   ├── search_doctor.py
│   ├── search_ordinary_user.py
│   ├── search_user_with_receipt.py
│   ├──user_validate.py
└── requirements.txt


Архитектура:
	архитектура соответствует 3 первым принципам SOLID  а как поттерн был выбран Factory . Проект состоит из несколько видов пользователей и товаров 
	и расширение проекта идет в пользу увеличение их количество нежели функционала и поэтому этот паттерн идеально подходит     