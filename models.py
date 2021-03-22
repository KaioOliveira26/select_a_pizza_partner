class Person():
    def __init__(self, name: str):
        self.name = name
        self.pizzas = {"Marguerita": 0, "Quatro queijos": 0, "Escarola": 0,
                       "Portuguesa": 0, "Frango+Catupiry": 0, "Napolitana": 0}

    def __str__(self):
        return f"Meu nome é {self.name} e minha pizza favorita é {max(self.pizzas, key=self.pizzas.get)}"

    def update_pizzas(self, pizzas_values: dict):
        for pizza_key in pizzas_values:
            self.pizzas[pizza_key] = 0

            if pizzas_values[pizza_key] >= 0 and pizzas_values[pizza_key] <= 5:
                self.pizzas[pizza_key] = pizzas_values[pizza_key]

    def get_a_buddy_for_pizza(self, people: list):
        buddy_negative_points = {}

        for person in people:
            if person.name != self.name:
                buddy_negative_points[person.name] = 0
                for pizza in person.pizzas:
                    buddy_negative_points.update({
                        person.name: max(buddy_negative_points[person.name] + person.pizzas[pizza], self.pizzas[pizza]) -
                        min(person.pizzas[pizza], self.pizzas[pizza])
                    })

        return min(buddy_negative_points, key=buddy_negative_points.get)
