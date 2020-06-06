from genderize import Genderize

def test_deve_retornar_feminino_quando_o_nome_vem_de_genero_feminino():
    detector = Genderize()
    genero = detector.get1(['Ana'])['gender']
    assert genero == "female"


def test_deve_retornar_masculino_quando_o_nome_vem_de_genero_masculino():
    detector = Genderize()
    genero = detector.get1(['Gleidson'])['gender']
    assert genero == "male"
