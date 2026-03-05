from run_checks import check, REPORT

def test_check_decorator_success():
    # On crée une fausse fonction avec ton décorateur
    @check("test_qui_passe")
    def faux_check_ok():
        return True

    # On la lance
    faux_check_ok()
    
    # On check si le dictionnaire a bien enregistré la réussite
    assert "test_qui_passe" in REPORT["checks"]
    assert REPORT["checks"]["test_qui_passe"] is True