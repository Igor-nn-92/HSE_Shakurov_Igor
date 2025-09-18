class CourtCase:
    def __init__(self, case_number):
        """
        Конструктор класса CourtCase
        
        Args:
            case_number (str): Номер дела (обязательный параметр)
        """
        self.case_number = case_number
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""
    
    def set_a_listening_datetime(self, datetime_str, location=""):
        """
        Добавляет в список listening_datetimes судебное заседание
        
        Args:
            datetime_str (str): Дата и время заседания
            location (str): Место проведения заседания (опционально)
        """
        hearing = {
            'datetime': datetime_str,
            'location': location
        }
        self.listening_datetimes.append(hearing)
    
    def add_participant(self, participant):
        """
        Добавляет участника в список case_participants
        
        Args:
            participant (str): ИНН или имя участника
        """
        if participant not in self.case_participants:
            self.case_participants.append(participant)
    
    def remove_participant(self, participant):
        """
        Убирает участника из списка case_participants
        
        Args:
            participant (str): ИНН или имя участника для удаления
        """
        if participant in self.case_participants:
            self.case_participants.remove(participant)
    
    def make_a_decision(self, verdict_text):
        """
        Вынести решение по делу, добавить verdict и сменить атрибут is_finished на True
        
        Args:
            verdict_text (str): Текст решения суда
        """
        self.verdict = verdict_text
        self.is_finished = True


# Пример использования
if __name__ == "__main__":
    # Создание экземпляра
    case = CourtCase("А40-123456/2024")
    
    # Добавление участников
    case.add_participant("7701234567")
    case.add_participant("7709876543")
    case.add_participant("Петров П.П.")
    
    # Назначение заседаний
    case.set_a_listening_datetime("2024-10-15 10:00", "Зал №5, Арбитражный суд")
    case.set_a_listening_datetime("2024-11-20 14:00", "Зал №3")
    
    # Удаление участника
    case.remove_participant("7709876543")
    
    # Вынесение решения
    case.make_a_decision("Иск удовлетворен полностью")
    
    # Проверка результата
    print(f"Дело {case.case_number}")
    print(f"Участники: {case.case_participants}")
    print(f"Заседания: {case.listening_datetimes}")
    print(f"Завершено: {case.is_finished}")
    print(f"Решение: {case.verdict}")
