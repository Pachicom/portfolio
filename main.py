#Импорт библиотек
import json
import re
from datetime import datetime
#Создание класса
class Portfolio:
    #Инициализация
    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.data = json.load(file)
    #Функция для дизайна
    def line(self):
        print("=" * 60)
    #Функция для отображения текста по центру
    def title(self, text):
        self.line()
        print(text.center(60))
        self.line()
    #Функция о себе
    def about(self):
        self.title("О СЕБЕ")
        about = self.data["about"]
        print(f"Имя: {about['name']}")
        print(f"Возраст: {about['age']}")
        print(f"Описание: {about['description']}")
        print("\nФакты обо мне:")
        for fact in about["facts"]:
            print(f"- {fact}")

    def goal(self):
        self.title("МОЯ ЦЕЛЬ")
        print(self.data["goal"])

    def it_story(self):
        self.title("КАК Я ПРИШЁЛ В IT")
        print(self.data["it_story"])

    def mentor(self):
        self.title("МОЙ МЕНТОР")
        mentor = self.data["mentor"]
        print(f"{mentor['name']}")
        print(mentor["description"])

    def progress(self):
        self.title("ТОЧКА А → ТОЧКА Б")
        progress = self.data["progress"]
        print("Точка А:")
        print(progress["point_a"])
        print("\nТочка Б:")
        print(progress["point_b"])

    def hobbies(self):
        self.title("ХОББИ И ИНТЕРЕСЫ")
        for hobby in self.data["hobbies"]:
            print(f"- {hobby}")

    def projects(self):
        self.title("МОИ ЛУЧШИЕ РАБОТЫ")
        for i, project in enumerate(self.data["projects"], start=1):
            print(f"{i}. {project['name']}")
            print(f"Описание: {project['description']}")
            print(f"Ссылка: {project['link']}")

    def github(self):
        self.title("МОЙ GITHUB")
        print(self.data["github"])

    def statistics(self):
        self.title("СТАТИСТИКА")
        age = self.data["about"]["age"]
        print(f"Возраст: {age}")
        print(f"Год: {datetime.now().year}")
        print(f"Количество проектов: {len(self.data['projects'])}")

    def menu(self):
        print("""
        ╔══════════════════════════════════════╗
        ║          МОЁ ПОРТФОЛИО               ║
        ║      Made for CAP Education          ║
        ╠══════════════════════════════════════╣
        ║ 1. О себе                            ║
        ║ 2. Моя цель                          ║
        ║ 3. Как я пришёл в IT                 ║
        ║ 4. Мой ментор                        ║
        ║ 5. Точка А → Точка Б                 ║
        ║ 6. Хобби и интересы                  ║
        ║ 7. Мои лучшие работы                 ║
        ║ 8. GitHub                            ║
        ║ 9. Статистика                        ║
        ║ 0. Выход                             ║
        ╚══════════════════════════════════════╝
        """)

    def get_choice(self):

        while True:
            try:
                choice = input("Выберите пункт: ")
                if re.fullmatch(r"[0-9]", choice):
                    return choice
            except IndexError:
                print("Неверный Индекс: Введите число от 0 до 9")

    def run(self):

        actions = {
            "1": self.about,
            "2": self.goal,
            "3": self.it_story,
            "4": self.mentor,
            "5": self.progress,
            "6": self.hobbies,
            "7": self.projects,
            "8": self.github,
            "9": self.statistics
         }

        while True:
            self.menu()
            choice = self.get_choice()
            if choice == "0":
                print("Спасибо за то, что просмотрели моё портфолио!")
                break
            actions[choice]()
            input("\nНажмите Enter для продолжения...")

portfolio = Portfolio("portfolio.json")
portfolio.run()
