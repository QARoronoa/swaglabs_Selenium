from faker import Faker

faker = Faker(locale="fr_FR")

class checkout_data:

    @staticmethod
    def formulaire():
        return {
            "firtsName" : faker.first_name(),
            "lastName": faker.last_name(),
            "cp": 92350
        }