from models import Person
import pytest


class TestPerson():
    def create_persons(self, number_of_people):
        people_names = ['tomas', 'josias',
                        'alexandra', 'natalia', 'lucia', 'diego']

        for index in range(number_of_people):
            yield Person(people_names[index])

    def test_creating_person(self):
        tomas = list(self.create_persons(1))[0]
        tomas.update_pizzas({"Napolitana": 5})

        expect = 'Meu nome é tomas e minha pizza favorita é Napolitana'
        assert str(expect) == str(tomas)

    def test_no_conflict_with_other_person(self):
        tomas, josias = list(self.create_persons(2))
        tomas.update_pizzas({"Napolitana": 5})
        josias.update_pizzas({"Escarola": 5})
        expect = 'Meu nome é josias e minha pizza favorita é Escarola'
        assert str(expect) == str(josias)

    def test_get_a_buddy(self):
        tomas, josias, alexandra, natalia = list(self.create_persons(4))

        tomas.update_pizzas(
            {"Napolitana": 1, "Escarola": 1, "Quatro queijos": 1})
        josias.update_pizzas(
            {"Napolitana": 2, "Escarola": 2, "Quatro queijos": 2})
        natalia.update_pizzas(
            {"Napolitana": 3, "Escarola": 2, "Quatro queijos": 2})
        alexandra.update_pizzas(
            {"Napolitana": 1, "Escarola": 2, "Quatro queijos": 2})

        assert tomas.get_a_buddy_for_pizza(
            [tomas, josias, alexandra, natalia]) == alexandra.name
