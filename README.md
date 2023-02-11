# Text-To-Symbol (TtoS)
**TextToSymbol** - это модуль предназначенный для произведения текста в красивые символы, таким способом, можно создать красивую подпись для своих проектов!

## Установка

Устанавливаем модуль через **pip:**
```
pip3 install ttos-py
```
или
```
python3 -m pip install ttos-py
```

## Пример
Для начала нам потребуется импортировать модуль, для удобства, назначим алиас text.

```
import TtoS as text
```

Далее, для работы создаем материал

```
txt = text.Image()
```

Используем наш материал и выводим через функцию print()

```
print(
    txt.output('fixees')
)

>> 🅵🅸🆇🅴🅴🆂
```

## Функция output()

Функция принимает 2 аргумента: name, theme

**Рассмотрим 1 вариацию тем для текста (theme='love'):**
```
print(
    txt.output(name='fixees', theme='love')
)
>> (っ◔◡◔)っ 🅵🅸🆇🅴🅴🆂 ♥
```

**2 Вариация:**
```
print(
txt.output(name='fixees', theme='made_by')
)
>> 𝙢𝙖𝙙𝙚 𝙗𝙮 🅵🅸🆇🅴🅴🆂
```


## Зависимости
* Python3


# Если у Вас есть вопросы -> [Разработчик](https://vk.me/fixees)

