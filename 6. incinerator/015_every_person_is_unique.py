class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender="unknown"):
        self.__dict__.update(locals())
        del self.__dict__['self']

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        return 2017 - int(self.birth_date.split('.')[2])

    def work(self):
        return {'unknown': 'Is a ',
                'male': 'He is a ',
                'female': 'She is a '}[self.gender] + self.job

    def money(self):
        amount = int(self.working_years * self.salary * 12)
        return "{:,}".format(amount).replace(",", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"


if __name__ == "__main__":

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith"
    assert p1.age() == 38
    assert p2.work() == "Is a designer"
    assert p1.money() == "648 000"
    assert p2.home() == "Lives in Vienna, Austria"

    print("OK")
