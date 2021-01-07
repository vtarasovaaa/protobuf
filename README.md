# Protobuf
### Библиотека кодирования-декодирования структур данных
 Версия: 0.1
 
 Автор: Тарасова Виктория (vtarasova394@gmail.com)
## Описание
Protocol Buffers — протокол сериализации (передачи) структурированных данных

## Методы

#### `create(filename)`
Метод, который принимает имя файла (формата `.proto`) и возвращает
класс, описанный в этом файле

## Описание и пример `proto` файла
```
message Car {
  required string model = 1;

  enum BodyType {
    sedan = 0;
    hatchback = 1;
    SUV = 2;
  }

  required BodyType type = 2 [default = sedan];
  optional string color = 3;
  required int32 year = 4;

  message Owner {
    required string name = 1;
    required string lastName = 2; 
    required int64 driverLicense = 3;
  }

  repeated Owner previousOwner = 5;
}
```
Ключевое слово `message` обозначает создание класса. 
Внутри фигурных скобок перечисляются атрибуты класса.

#### Типы атрибутов 
- required

Означает, что поле обязательное и его нужно указать при инициализации класса

- optional 

Необязательное поле, если при создании экземпляра не указан, то указывается значение по умолчанию 
(Пока не реализовано)

- repeated 

Пока не реализовано

## Состав
- Библиотека кодирования-декодирования структур данных: `Protobuf.py`
- Модули: `protobuf`
- Тесты: `tests`
- Прото-файлы для тестов: `tests files`
