from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender="unknown"):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        birth_date = datetime.strptime(self.birth_date, "%d.%m.%Y")
        cur_date = datetime.strptime("01.01.2018", "%d.%m.%Y")
        delta = cur_date - birth_date
        age = int(delta.days // 365.2425)
        return age

    def work(self):
        if self.gender == "male":
            out = f"He is a {self.job}"
        elif self.gender == "female":
            out = f"She is a {self.job}"
        else:
            out = f"Is a {self.job}"

        return out

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
