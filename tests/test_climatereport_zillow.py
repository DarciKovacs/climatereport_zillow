from climatereport_zillow import extract_address


def test_zipcode():
    example = 'https://www.zillow.com/homedetails/13353-Cavandish-Ln-Moreno-Valley-CA-92553/18008847_zpid/'
    expected = 92553
    actual = extract_address.make_zipcode(example)
    assert actual == expected

def test_state():
    example = 'https://www.zillow.com/homedetails/13353-Cavandish-Ln-Moreno-Valley-CA-92553/18008847_zpid/'
    expected = "CA"
    actual = extract_address.make_state(example)
    assert actual == expected

