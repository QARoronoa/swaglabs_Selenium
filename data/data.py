from faker import Faker

faker = Faker(locale="fr_FR")

class loginPageData :

    test_data_standard_user = [{
        "username" : "standard_user",
        "password" : "secret_sauce"
    }]

    test_data_incorrect_user = [{
        "username" : faker.name(),
        "password" : faker.password()
    }]

class datacheckoutInformation :
        
    test_data_checkout = [{
        "firstname" : faker.name(),
        "lastname" : faker.last_name(),
        "zipCode" : faker.postcode()
    }]
