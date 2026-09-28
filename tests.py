from main import Person

def test_person():
    p = Person("Hans", 18)
        
    vorher = p.alter
    p.altern(1)
    
    assert p.alter > vorher
    assert p.alter == 19

    p.altern(-100)  # Das sollte nicht funktionieren dürfen
    assert p.alter > 0, "Die Person hat ein negatives Alter!"        