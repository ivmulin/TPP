"""
raptor - билето-генераптор
"""


from random import randint

# Макросы файла с вопросами
CATEGORY = "Тема:"

# Макросы формата билетов
STUDENT = "<student>"  # имя студента
CAT = "<cat>"  # cat = category = тема билета
QUESTION = "<question>"  # вопрос
QUESTION_ENTRY = "<question_pos>"  # номер вопроса в списке вопросов
QUESTION_NO = "<question_no>"  # номер вопроса по теме в билете
CAT_NO = "<cat_no>"  # номер темы в билете
BILL_NO = "<bill_no>"  # номер билета

# Обязательные макросы форматирования
TASK_START = "%("  # обязана содержать %
TASK_END = "%)"  # обязана содержать %


"""
# Инструкция по форматированию вывода.



Это должна быть f-строка, использующая макросы {TASK_START} и {TASK_END} (в этом порядке
и ровно 1 раз!). Можно также использовать иные макросы, указанные выше; обратите внимание,
что необходимо заключить их в {}, поскольку используется форматирование на языке python.
Строка передаётся в качестве аргумента fmt в класс GenerateBills.


Строка в обшем случае имеет вид
'<что угодно>[{TASK_START}<формат билетов>{TASK_END}|<sep1>|<sep2>|<sep3>]<что угодно>'

(Обратите внимание на то, что [ и ] также обязательны к использованию.)

* <sep1> - это разделитель вопросов
* <sep2> - это разделитель тем
* <sep3> - это разделитель билетов

Для <sep1>, <sep2> и <sep3> выставлены значения по умолчанию, равные ',', ';' и '\n' соот-
ветственно, поэтому можно не указывать их (при этом не нужно писать разделитель | ).

Действуют следующие правила:
1. Макросы {TASK_START} и {TASK_END} обязательны к использованию. Они обозначают начало и
конец подстроки, содержащей формат вопросов.{TASK_START} и {TASK_END} должны быть уникаль-
ными.
2. В подстроке <что угодно> будет корректно работать только макрос {STUDENT}, обозначающий
имя студента.
3. <формат билетов> очень любит макросы.

Ниже приведены некоторые примеры использования этой технологии.
"""


# Примеры форматирования
OUT_FORMAT1 = f"\
Билет № {BILL_NO}\n\
1. [Вопросы по теме {CAT}:\n{TASK_START}{CAT_NO}.\
{QUESTION_NO}. {QUESTION}{TASK_END}|\n|\n{CAT_NO}. |\n\n]"

OUT_FORMAT2 = f"""\
--- Билет для студента {STUDENT} ---
* [Вопросы по теме {CAT}:\n  - {TASK_START}{QUESTION}{TASK_END}|\n  - |\n* |\n\n]"""

# OUT_FORMAT1 использует почти все доступные макросы во всём их многообразии


class InvalidQuestionFileError(Exception):
    """
    Исключение, вызываемое, если файл с вопросами некорректен.
    """

    def __init__(self, message):
        super().__init__(message)


class InvalidExamFormatError(Exception):
    """
    Исключение, вызываемое при неправильном заполнении формата билетов.
    """

    def __init__(self, message):
        super().__init__(message)


class InvalidOutputFormatError(Exception):
    """
    Исключение, вызываемое при неверном составлении формата файла с билетами.
    """

    def __init__(self, message):
        super().__init__(message)


class BoringExamError(Warning):
    """
    Предупреждение, вызываемое, если экзамен претендует на скуку.
    """

    def __init__(self, message):
        super().__init__(message)


def read_questions(filename):
    """
    Считывает вопросы из указанного файла. Возвращает словарь.
    """
    questions = {}
    current_category = '\0'

    with open(filename, 'r', encoding="utf-8") as file:
        lineno = 0
        while (line := file.readline()):
            lineno += 1

            if line.strip() == "":
                continue

            # Если строка начинается с CATEGORY, то начинается блок вопросов по теме
            if line.startswith(CATEGORY):
                line = line.replace(CATEGORY, "", 1)
                line = line.strip()

                # Добавляем тему в словарь, коли её ещё нет
                if line not in questions:
                    questions[line] = []

                current_category = line

            elif '.' in line:
                # Если line есть - предположительно - вопрос
                question_no, question = line.split('.', 1)

                if not question_no.isnumeric():
                    # Если номер вопроса - не число
                    raise InvalidQuestionFileError(
                        f"В файле {filename} в строке {lineno} неправильно\
указан номер вопроса: {question_no}")
                question_no = int(question_no)
                question = question[:-1].strip()

                if current_category == '\0':
                    # Если не указана тема вопроса
                    raise InvalidQuestionFileError(
                        f"В файле {filename} в строке {lineno} не задана\
тема вопроса № {question_no}. Допишите\nТема: <тема вопроса>")

                questions[current_category].append(question)

            else:
                if CATEGORY in line:  # проблема в теме
                    raise InvalidQuestionFileError(
                        f"В файле {filename} в строке {lineno}\n{line}неправильно указана тема.")
                # иначе проблема в вопросе
                raise InvalidQuestionFileError(
                    f"В файле {filename} строка {lineno}\n{line}имеет\
неправильный формат вопроса. Требуемый формат:\n<номер вопроса>.\
<вопрос>\nЯ не буду больше работать.")

    return questions


class GenerateBills:
    """
    Генератор списка билетов.
    """

    def __init__(
            self, bill_format_str, students_list="./data/FIO.txt",
            questions_list="./data/Questions.txt", fmt=OUT_FORMAT2):
        """
        Конструктор. Как будто непонятно...
        """
        self.students_list = students_list
        self.questions_list = questions_list
        self.fmt = fmt

        with open(students_list, 'r', encoding="utf-8") as stud_file:
            self.students = stud_file.read().split('\n')[:-1]

        self.questions = read_questions(questions_list)

        self.bill_format = self.check_bills_format(bill_format_str)

        self.bills = self.generate_bills()

        self.compose_bills()

    def check_bills_format(self, bill_format_str):
        """
        Проверяет корректность формата экзамена.

        Переменная bill_format_str должна быть строкой вида
        "<тема 1>-<число вопросов 1> <тема 2>-<число вопросов 2> ..."
        """

        bill_format_str = bill_format_str.strip()
        tokens = bill_format_str.split()
        bill_format = {}

        for t in tokens:
            cat, cat_amount = t.split('-', 1)

            if cat not in self.questions:
                # Если требуются по теме, к которой студенты не готовились
                raise InvalidExamFormatError(
                    f"Темы {cat} нет в списке вопросов {self.questions_list}.")

            if not cat_amount.isnumeric():
                raise InvalidExamFormatError(f"{cat_amount} не есть число.")

            cat_amount = int(cat_amount)
            que_amount = len(self.questions[cat])

            # cat = category
            if cat in bill_format and bill_format[cat] != cat_amount:
                # Если по теме cat требуют разное кол-во вопросов
                raise InvalidExamFormatError(
                    f"Не могу определить число билетов по теме {cat}: \
{bill_format[cat]} или {cat_amount}?")
            if cat_amount == 0:
                # Коли нет вопросов...
                raise BoringExamError(
                    f"По теме {cat} затребовано {cat_amount} вопросов. Так скучно!")

            # Иначе добавляем в словарь
            bill_format[cat] = cat_amount

            if que_amount < cat_amount:
                # Если требуется больше вопросов, чем есть в списке
                raise InvalidExamFormatError(
                    f"Недостаёт {cat_amount + 1 - que_amount} вопросов по\
теме {cat} в файле {self.questions_list}.")
            if que_amount == cat_amount:
                # Если у всех студентов одни и те же вопросы по теме cat
                raise BoringExamError(
                    f"У всех студентов будет одинаковое количество вопросов по теме {cat}.")

        return bill_format

    def choose_questions(self, cat, cat_amount):
        """
        Псевдослучайно выбирает cat_amount вопросов по теме cat.
        """

        queue = []
        options = self.questions[cat].copy()

        while cat_amount:
            index = randint(0, len(options) - 1)
            queue.append((index + 1, options.pop(index)))
            cat_amount -= 1

        return queue

    def generate_bills(self):
        """
        Создаёт билеты для каждого студента в списке.
        """

        bills = {s: [] for s in self.students}

        for student in bills:
            list_of_tasks = {}
            for cat, cat_amount in self.bill_format.items():  # cat = category
                list_of_tasks[cat] = self.choose_questions(cat, cat_amount)
            bills[student] = list_of_tasks

        return bills

    def compose_bills(self, out_name="Билеты.txt"):
        """
        Записывает билеты с указанным форматированием
        """

        if self.fmt.count('[') != self.fmt.count(']') or self.fmt.count('[') not in (0, 1):
            # Если не закрыты скобки [ ] либо их больше, чем нода
            raise InvalidOutputFormatError(
                "Неправильное применение скобок [ ]")

        a = self.fmt.find('[')
        b = self.fmt.find(']')

        if a > b:
            # Если ] [
            raise InvalidOutputFormatError(
                "Скобки [ ] в обратном порядке.")

        # sample1 - шаблон вопроса
        # sample2 - шаблон билета
        sample2, *separators = self.fmt[a+1:b].split('|')

        if TASK_START == TASK_END:
            raise InvalidOutputFormatError(
                "Макросы TASK_START и TASK_END должны быть уникальными")

        if sample2.count(TASK_START) != sample2.count(TASK_END):
            raise InvalidOutputFormatError(
                f"{TASK_END} не закрывает {TASK_START}")
        # иначе кол-во TASK_START == кол-ву TASK_END

        if sample2.count(TASK_START) == 0:
            raise BoringExamError(
                f"В строке форматирования:\n{self.fmt}\nсказано, что\
вопросов не предусмотрено. Вы вообще планируете спрашивать у студентов что-либо?")
        if sample2.count(TASK_START) > 1:
            raise InvalidOutputFormatError(
                "Проблема с количеством TASK_START или TASK_END в\
строке форматирования (их количество доолжно быть ровно 1)")

        c = sample2.find(TASK_START)
        d = sample2.find(TASK_END)

        if c > d:
            # Если TASK_END TASK_START
            raise InvalidOutputFormatError(
                f"{TASK_START} и {TASK_END} в обратном порядке.")

        sample1 = sample2[c + len(TASK_START): d]

        if '%' not in TASK_START:
            raise InvalidOutputFormatError("TASK_START должен содержать %")

        if '%' not in TASK_END:
            raise InvalidOutputFormatError("TASK_END должен содержать %")

        sample2 = sample2.replace(TASK_START, "")
        sample2 = sample2.replace(TASK_END, "")

        # sep1 - разделитель между вопросами по теме
        # sep2 - разделитель между темами
        # sep3 - разделитель между билетами
        if len(separators) == 0:
            sep1, sep2, sep3 = ',', ';', '\n'
        elif len(separators) == 1:
            sep1, sep2, sep3 = *separators, ';', '\n'
        elif len(separators) == 2:
            sep1, sep2, sep3 = *separators, '\n'
        elif len(separators) == 3:
            sep1, sep2, sep3 = separators
        else:
            raise InvalidOutputFormatError("Слишком много разделителей |")

        string = ""
        counter3 = 1

        for student in self.bills:
            bill = ""
            counter2 = 1
            for cat in self.bills[student]:
                bill += sample2.replace(CAT, cat)

                tasks = ""
                counter1 = 1
                for q_no, q in self.bills[student][cat]:
                    some_str = sample1.replace(QUESTION_ENTRY,
                                               str(q_no)).replace(QUESTION, q)
                    some_str = some_str.replace(QUESTION_NO, str(counter1))

                    tasks += some_str

                    if counter1 != len(self.bills[student][cat]):
                        tasks += sep1
                    counter1 += 1

                bill = bill.replace(sample1, tasks)
                bill = bill.replace(CAT_NO, str(counter2))

                if counter2 != len(self.bills[student]):
                    bill += sep2
                counter2 += 1

            if counter3 != len(self.bills):
                bill += sep3

            _ = self.fmt.replace(self.fmt[a:b+1], bill)
            _ = _.replace(BILL_NO, str(counter3))
            _ = _.replace(STUDENT, student)

            string += _
            counter3 += 1

        print(string, "\n---------", sep='\n')

        with open(out_name, 'w', encoding="utf-8") as file:
            file.write(string)
            file.write('\n\0')

        print(f"Сохранено в {out_name}")


if __name__ == "__main__":
    GenerateBills("cd-2 ab-1", fmt=OUT_FORMAT1)
