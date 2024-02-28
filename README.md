# algopro-23
**Алгоритмизация и программирование 2023-2024**  
**БЕЛЯКОВ Андрей Юрьевич** [telegram](https://t.me/AndreyPerm)  
[Анкетирование и Тестирование - EXAM](http://exam.1gb.ru/)  
> [РЕЙТИНГ](https://docs.google.com/spreadsheets/d/1KIFBWhesFTBvYPpPTZZnEa5Ka1p1cyUzJFHp1cecO8Y/edit?usp=sharing)  

---  

Объём учебной дисциплины:  
| семестр | Лекций | ЛабРаб | Отчётность |
| :-: | :-: | :-: | :-: |
| 1 | 14 | 11 | Экзамен |
| 2 | 14 | 11 | Экзамен |

---  

### Дистанционные занятия тут:  
* [сервер BBB](https://bbb.psaa.ru/rooms/clu-pi0-lck-coa/join)  
* [Zoom](https://us04web.zoom.us/j/6931731236?pwd=T1lNamFoMjJtMHlSbWVKZHF2d3Qwdz09)  
* [Discord](https://discord.gg/ZK4kgdn)  

---  

> [Учебник Алгоритмы на Python](https://pcoding.ru/pdf/PythonJunior.pdf)  
> [Учебник Тектовые файлы на Python](https://pcoding.ru/pdf/PythonJunior_files.pdf)  
> [ГОСТ 19.701-90 Схемы алгоритмов...](https://pcoding.ru/gost/GOST_19.701-90_Алгоритмы.pdf)  
> [Как расшарить приватный репозиторий](https://pcoding.ru/pdf/shareGit.pdf)  
> [Стандарт PEP 8 - первоисточник, Предложения по улучшению Python](https://peps.python.org/pep-0008/)  
> [Стандарт PEP 8 по оформлению кода на Python - Python Enhancement Proposal](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)  
[Структуры данных в Python](https://docs.python.org/3/tutorial/datastructures.html)  

---  

```txt
* как проверить версию Python
python -V

* как удалить Python
sudo apt remove python3
sudo apt autoclean && sudo apt autoremove

* установить требуемую версию Python, например, 3.12

sudo apt update

sudo apt install wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

- загрузить архив требуемого питона: https://www.python.org/downloads/source/
- и распаковать этот архив:
tar -Jxvf Python-3.12.2.tar.xz

- перейти в папку
cd Python-3.12.2

- конфигурировать
./configure --enable-optimizations --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"

- установить в папку /usr/local/bin
sudo make -j4 && sudo make altinstall

- Check the version of Python and pip installed.

$ python3.12 --version
Python 3.12.2

$ pip3.12 --version
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

- как устанавливать пакеты
sudo pip3.12 install module-name
- например:
sudo pip3.12 install beautifulsoup4

- как установить виртуальное окружение
python3.12 -m venv venv
- активировать
source venv/bin/activate

- установить локально пакеты и работать

- деактивировать
deactivate

---

* как установить в linux pip
sudo apt update
sudo apt install python3-pip

* проверить версию pip
pip3 --version

---

* как установить в linux библиотеку pillow
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow

* как установить в linux библиотеку tkinter
sudo apt update
sudo apt install python3-tk

* Установить шрифт Fira Code
sudo apt update
sudo apt install fonts-firacode
```

```txt
X.Y.Z Version
MAJOR version -- when you make incompatible API changes,
MINOR version -- when you add functionality in a backwards-compatible manner
PATCH version -- when you make backwards-compatible bug fixes.
```
[Управляющие символы](https://ru.wikipedia.org/wiki/%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B5_%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B)  
[Регулярка для проверки email](https://pdw.ex-parrot.com/Mail-RFC822-Address.html)  

---
