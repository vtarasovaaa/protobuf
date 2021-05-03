# Protobuf
### Библиотека кодирования-декодирования структур данных
 Версия: 1.1
 
 Автор: Тарасова Виктория (vtarasova394@gmail.com)
## Описание
Protocol Buffers — протокол сериализации (передачи) структурированных данных

## Требования 
Версия не ниже `Python 3.7`

## Как использовать?
- `import Protobuf as pb` 

Делаете импорт модуля для работы с ним и пользуетесь прекрасными методами, 
которые описаны ниже :)

## Методы

#### `create(filename)`
Метод, который принимает имя файла (формата `.proto`) и возвращает
класс, описанный в этом файле

`Car = pb.create('car.proto')`

После этого можно создать экземпляр класса `Car`: 

`car = Car(type=Car.BodyType.sedan, year=2000,
          previousOwner=Car.Owner('Viktoria', 'Tarasova', 12345))`

###В классе есть пара методов:

#### `to_file(filename)`

Метод сереализует данные в бинарный файл
`car.to_file(car.bin)`
#### `from_file(filename)`
Метод десереализует данные из бинарного файла
`car2 = Сar.from_file(car.bin)`


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

- repeated 

Пока не реализовано

## Состав
- Библиотека кодирования-декодирования структур данных: `Protobuf.py`
- Модули: `protobuf`
- Тесты: `tests`
- Прото-файлы для тестов: `tests files`
