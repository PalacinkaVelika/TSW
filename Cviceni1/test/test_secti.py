from app import secti

#testový případ (test case)
# def test_secti_dve_cela_kladna_cisla():
#     #AAA framework(Arrange, Act, Assert)
#     #Arrange
#     cislo1 = 2
#     cislo2 = 5
#     ocekavany_vysledek = 7
#     #Act
#     vystup = secti(a=cislo1, b=cislo2)
#     #Assert
#     assert vystup == ocekavany_vysledek

# def test_secti_dve_cela_zaporna_cisla():
#     cislo1 = -2
#     cislo2 = -3
#     ocekavany_vysledek = -5
#     vystup = secti(a=cislo1, b=cislo2)
#     assert vystup == ocekavany_vysledek

@pytest.mark.parametrize("cisla, ocekavany_vysledek", [
    ((2, 5), 7),
    ((-2, -3), -5)
    ((1.0, -2.0), -1.0),
    (("1.0", "traktor"), "1.0traktor")
])

def test_secti_dve_cela_cisla(cisla, ocekavany_vysledek):
    assert secti(a=cisla[0], b=cisla[1]) == ocekavany_vysledek