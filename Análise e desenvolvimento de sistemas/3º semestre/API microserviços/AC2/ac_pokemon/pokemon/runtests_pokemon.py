import unittest
from requests import api



class TestPokeapi(unittest.TestCase):
    
    def test_01a_ok(self):
        # verificar_online("pokeapi")
        self.assertEqual(nome_do_pokemon(1), "bulbasaur")
        self.assertEqual(nome_do_pokemon(55), "golduck")
        self.assertEqual(nome_do_pokemon(25), "pikachu")
        self.assertEqual(nome_do_pokemon(700), "sylveon")
        self.assertEqual(nome_do_pokemon(807), "zeraora")

    
    def test_02a_ok(self):
        self.assertEqual(numero_do_pokemon("marill"), 183)

    
    def test_02b_caps(self):
        self.assertEqual(numero_do_pokemon("EEVEE"), 133)
        self.assertEqual(numero_do_pokemon("Psyduck"), 54)
        self.assertEqual(numero_do_pokemon("SkiTtY"), 300)
        self.assertEqual(numero_do_pokemon("Zeraora"), 807)

    
    def test_02c_nao_existe(self):
        pokemon_nao_existe(lambda : numero_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : numero_do_pokemon("SpiderMan"), self)

    
    def test_03a_ok(self):
        self.assertEqual(color_of_pokemon("marill"), "blue")
        self.assertEqual(color_of_pokemon("togekiss"), "white")
        self.assertEqual(color_of_pokemon("magneton"), "gray")

    
    def test_03b_caps(self):
        self.assertEqual(color_of_pokemon("EEVEE"), "brown")
        self.assertEqual(color_of_pokemon("Psyduck"), "yellow")
        self.assertEqual(color_of_pokemon("SkiTtY"), "pink")
        self.assertEqual(color_of_pokemon("GASTLY"), "purple")
        self.assertEqual(color_of_pokemon("LeDyBa"), "red")
        self.assertEqual(color_of_pokemon("Torterra"), "green")
        self.assertEqual(color_of_pokemon("xurkiTree"), "black")

    
    def test_03c_nao_existe(self):
        pokemon_nao_existe(lambda : color_of_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("batman"), self)
        pokemon_nao_existe(lambda : color_of_pokemon("SpiderMan"), self)

    
    def test_04a_ok(self):
        self.assertEqual(cor_do_pokemon("marill"), "azul")
        self.assertEqual(cor_do_pokemon("togekiss"), "branco")

    
    def test_04b_caps(self):
        self.assertEqual(cor_do_pokemon("EEVEE"), "marrom")
        self.assertEqual(cor_do_pokemon("Psyduck"), "amarelo")
        self.assertEqual(cor_do_pokemon("SkiTtY"), "rosa")
        self.assertEqual(cor_do_pokemon("magneton"), "cinza")
        self.assertEqual(cor_do_pokemon("GASTLY"), "roxo")
        self.assertEqual(cor_do_pokemon("LeDyBa"), "vermelho")
        self.assertEqual(cor_do_pokemon("Torterra"), "verde")
        self.assertEqual(cor_do_pokemon("xurkiTree"), "preto")

    
    def test_04c_nao_existe(self):
        pokemon_nao_existe(lambda : cor_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : cor_do_pokemon("SpiderMan"), self)

    
    def test_05a_ok(self):
        self.assert_equals_unordered_list(["grama"], tipos_do_pokemon("chikorita"))
        self.assert_equals_unordered_list(["terra"], tipos_do_pokemon("hippowdon"))
        self.assert_equals_unordered_list(["normal", "fada"], tipos_do_pokemon("jigglypuff"))
        self.assert_equals_unordered_list(["fogo"], tipos_do_pokemon("darumaka"))
        self.assert_equals_unordered_list(["pedra", "voador"], tipos_do_pokemon("archeops"))

    
    def test_05b_caps(self):
        self.assert_equals_unordered_list(["voador", "noturno"], tipos_do_pokemon("murKrow"))
        self.assert_equals_unordered_list(["água", "elétrico"], tipos_do_pokemon("cHinChou"))
        self.assert_equals_unordered_list(["lutador", "fantasma"], tipos_do_pokemon("MARSHADOW"))
        self.assert_equals_unordered_list(["aço"], tipos_do_pokemon("KLINK"))
        self.assert_equals_unordered_list(["lutador", "inseto"], tipos_do_pokemon("Heracross"))
        self.assert_equals_unordered_list(["veneno", "noturno"], tipos_do_pokemon("DRAPION"))
        self.assert_equals_unordered_list(["psíquico", "gelo"], tipos_do_pokemon("JYNX"))
        self.assert_equals_unordered_list(["dragão"], tipos_do_pokemon("dRaTiNi"))

    
    def test_05c_nao_existe(self):
        pokemon_nao_existe(lambda : tipos_do_pokemon("DOBBY"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("batman"), self)
        pokemon_nao_existe(lambda : tipos_do_pokemon("SpiderMan"), self)

    
    def test_06a_ok(self):
        self.assertEqual(evolucao_anterior("togetic"), "togepi")

    
    def test_06b_caps(self):
        self.assertEqual(evolucao_anterior("togeKiss"), "togetic")
        self.assertEqual(evolucao_anterior("EEleKtriK"), "tynamo")
        self.assertEqual(evolucao_anterior("EELEKTROSS"), "eelektrik")
        self.assertEqual(evolucao_anterior("Pikachu"), "pichu")
        self.assertEqual(evolucao_anterior("rAiChu"), "pikachu")

    
    def test_06c_nao_tem(self):
        self.assertIs(evolucao_anterior("togepi"), None)
        self.assertIs(evolucao_anterior("TYNAMO"), None)
        self.assertIs(evolucao_anterior("Pichu"), None)

    
    def test_06d_nao_existe(self):
        pokemon_nao_existe(lambda : evolucao_anterior("DOBBY"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("Peppa-Pig"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("batman"), self)
        pokemon_nao_existe(lambda : evolucao_anterior("SpiderMan"), self)

    
   
    
    def test_07a_simples(self):
        self.assertEqual(nivel_do_pokemon("blastoise",   110000), 49) # 4
        self.assertEqual(nivel_do_pokemon("mewtwo",     1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",       900),  8) # 1
        self.assertEqual(nivel_do_pokemon("Magikarp",   1000000), 92) # 1
        self.assertEqual(nivel_do_pokemon("SLOWBRO",      65000), 40) # 2
        self.assertEqual(nivel_do_pokemon("OcTiLLeRy",   280000), 65) # 2
        self.assertEqual(nivel_do_pokemon("FRAXURE",     280000), 60) # 1
        self.assertEqual(nivel_do_pokemon("lunatone",     20000), 29) # 3
        self.assertEqual(nivel_do_pokemon("skitty",       50000), 39) # 3
        self.assertEqual(nivel_do_pokemon("torchic",      40000), 35) # 4
        self.assertEqual(nivel_do_pokemon("ODDISH",        5000), 19) # 4

    
    def test_07b_complexos(self):
        self.assertEqual(nivel_do_pokemon("zangoose",      9000), 17) # 5
        self.assertEqual(nivel_do_pokemon("milotic",      65000), 37) # 5
        self.assertEqual(nivel_do_pokemon("Lumineon",    160000), 55) # 5
        self.assertEqual(nivel_do_pokemon("NINJASK",     300000), 72) # 5
        self.assertEqual(nivel_do_pokemon("zangoose",    580000), 97) # 5
        self.assertEqual(nivel_do_pokemon("makuhita",       600), 10) # 6
        self.assertEqual(nivel_do_pokemon("gulpin",        7000), 21) # 6
        self.assertEqual(nivel_do_pokemon("seviper",     150000), 50) # 6
        self.assertEqual(nivel_do_pokemon("drifblim",   1000000), 87) # 6

    
    def test_07c_limites(self):
        self.assertEqual(nivel_do_pokemon("pinsir",           0),   1) # 1
        self.assertEqual(nivel_do_pokemon("bibarel",          0),   1) # 2
        self.assertEqual(nivel_do_pokemon("aipom",            0),   1) # 3
        self.assertEqual(nivel_do_pokemon("Makuhita",         0),   1) # 6
        self.assertEqual(nivel_do_pokemon("Magikarp",      1249),   9) # 1
        self.assertEqual(nivel_do_pokemon("MeTaPoD",        999),   9) # 2
        self.assertEqual(nivel_do_pokemon("Magikarp",      1250),  10) # 1
        self.assertEqual(nivel_do_pokemon("Butterfree",    1000),  10) # 2
        self.assertEqual(nivel_do_pokemon("charmeleon",   29948),  32) # 4
        self.assertEqual(nivel_do_pokemon("charmeleon",   29949),  33) # 4
        self.assertEqual(nivel_do_pokemon("hariyama",     71676),  40) # 6
        self.assertEqual(nivel_do_pokemon("hariyama",     71677),  41) # 6
        self.assertEqual(nivel_do_pokemon("togePI",      799999),  99) # 3
        self.assertEqual(nivel_do_pokemon("gengar",     1059859),  99) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    599999),  99) # 5
        self.assertEqual(nivel_do_pokemon("SWALot",     1639999),  99) # 6
        self.assertEqual(nivel_do_pokemon("sYLVEON",    1000000), 100) # 2
        self.assertEqual(nivel_do_pokemon("Jigglypuff", 1000000), 100) # 3
        self.assertEqual(nivel_do_pokemon("LEDIAN",      800000), 100) # 3
        self.assertEqual(nivel_do_pokemon("vaPorEON", 999999999), 100) # 2
        self.assertEqual(nivel_do_pokemon("VILEPLUME",  1059860), 100) # 4
        self.assertEqual(nivel_do_pokemon("zangoose",    600000), 100) # 5
        self.assertEqual(nivel_do_pokemon("SWALOT",     1640000), 100) # 6

    
    def test_07d_nao_existe(self):
        pokemon_nao_existe(lambda : nivel_do_pokemon("DOBBY", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("Peppa-Pig", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("batman", 1234), self)
        pokemon_nao_existe(lambda : nivel_do_pokemon("SpiderMan", 1234), self)

        

    



def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPokeapi)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)


from requests import api, exceptions
from pokemon import *

def verificar_online(desejado):

    def pokeapi_online():
        try:
            resposta1 = api.get(f"http://127.0.0.1:8000")
            if resposta1.status_code == 200 and resposta1.json()['pokemon'] == f'http://pokeapi.co/api/v2/':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    def treinador_online():
        try:
            resposta2 = api.get(f"http://127.0.0.1:9000/hello")
            if resposta2.status_code == 200 and resposta2.text == 'Pikachu, eu escolho você!':
                return "online"
            return "zumbi"
        except exceptions.ConnectionError as x:
            return "offline"
        except:
            return "zumbi"

    # if site_treinador != "http://127.0.0.1:9000" or site_pokeapi != "http://127.0.0.1:8000": raise Exception("As URLs para as APIs estão incorretas.")
    y = pokeapi_online()
    z = treinador_online()

    if y in ("zumbi","offline"): raise Exception("Para poder rodar os testes, você precisa de acesso ao pokeapi. Verifique se você tem esse acesso.")
    if desejado == "pokeapi+treinador":
        if y == "zumbi" or z == "zumbi": raise Exception("Os servidores aparentemente não estão em funcionamento. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "offline" and z == "offline": raise Exception("Os servidores estão off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        if y == "online" and z == "offline": raise Exception("O treinador está off-line. A partir do teste 09, ele precisa estar online")
        if y == "offline" and z == "online": raise Exception("O pokeapi está off-line. Estes testes só devem ser executados com ambos os servidores on-line.")
        assert y == "online" and z == "online"
    

def verificar_erro(interno, tipo_erro, tests = None):
    if tests is None:
        try:
            interno()
        except Exception as x:
            assert type(x) is tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}."
        else:
            assert False, f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi."
    else:
        try:
            interno()
        except Exception as x:
            tests.assertIs(type(x), tipo_erro, f"Esperava-se que um erro do tipo {tipo_erro.__name__}, mas obteve-se uma do tipo {x.__class__.__name__}.")
        else:
            tests.fail(f"Esperava-se que um erro do tipo {tipo_erro.__name__} fosse produzido, mas não foi.")

def pokemon_nao_existe(interno, tests = None):
    verificar_erro(interno, PokemonNaoExisteException, tests)


def pokemon_ja_cadastrado(interno, tests = None):
    verificar_erro(interno, PokemonJaCadastradoException, tests)

def valor_errado(interno, tests = None):
    verificar_erro(interno, ValueError, tests)

def assert_equals_unordered_list(esperada, obtida, tests = None):
    error_string = f"Esperava-se que o resultado fosse {esperada}, mas foi {obtida}."
    if tests is None:
        assert len(esperada) == len(obtida), error_string
        for item in esperada:
            assert item in obtida, error_string
    else:
        tests.assertEqual(len(esperada), len(obtida), error_string)
        for item in esperada:
            tests.assertIn(item, obtida, error_string)

def assert_equals_unordered_list_clear(self, esperada, obtida):
    assert_equals_unordered_list(esperada, obtida, self)


TestPokeapi.assert_equals_unordered_list = assert_equals_unordered_list_clear

try:
    import sys
    sys.path.append("../")
    from pokemon import *
except:
    pass


if __name__ == '__main__':
    runTests()
