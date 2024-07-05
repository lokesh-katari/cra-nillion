from nada_dsl import *

def nada_main():
    nilla_the_dog = Party(name="Nilla 🐶")

    secret_int_1 = SecretInteger(Input(name="my_secret_1", party=nilla_the_dog))
    secret_int_2 = SecretInteger(Input(name="my_secret_2", party=nilla_the_dog))
    secret_int_3 = SecretInteger(Input(name="my_secret_3", party=nilla_the_dog))

    total_addition = secret_int_1 + secret_int_2
    total_multiplication = total_addition * secret_int_3
    final_result = total_multiplication - secret_int_1

    return [Output(final_result, "my_output", nilla_the_dog)]
