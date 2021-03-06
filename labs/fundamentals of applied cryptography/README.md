# О лабораторных работах

## Структура

Лабораторные работы не представляют из себя что-то интересное: достаточно простая реализация методов шифрования их следующего списка:

- Лабораторная работа №1 (несколько методов шифрования):
  - Метод Цезаря с ключевым словом
  - Метод Цезаря по аффинной перестановке
  - Метод двойных квадратов Уинстона
  - Метод перестановки
- Лабораторная работа №2 (протокол Шамира)
- Лабораторная работа №3 (RSA шифрование)
- Лабораторная работа №4 (схема Эль-Гамаль)

## Оценка проделанной работе

Если честно, работа проделана плохо. Сами по себе методы реализованы нормально, но они нуждаются в оптимизации, так как в коде я уже нашел несколько "Бутылочных горлышек", которые могут стать критичными в некоторых ситуациях. Пока я выполняю шифровку и расшифровку на небольших фразах, но если понадобится сделать всё то же самое, но с большими тестами, то реализованные алгоритмы шифрования и дешифрования покажут себя не с лучшей стороны. Благо, в первой лабораторной работе происходит формирование шифрованного и дешифрованного алфавита, что не сильно будет влиять в работе с большими тестами.

Ещё из минусов могу отметить то, что UI не очень дружелюбен к пользователю. Как-то изменить это я не могу, но могу изменить подход к написанию непосредственно UI: _Для дальнейших лабораторных работ (2 и дальше) планирую написать web-интерфейс с back-end'ом на Flask или Django._
