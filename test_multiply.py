from multiply import multiply

def test_multiply():
# arrange
    a=2
    b=3

# act

    result =multiply(a,b)


# assert

    assert result==6


def test_negative():

#arrange    
    a=2
    b=-3
#act
    answer=multiply(a,b)
#
    assert answer==-16 ,"when you multiply negative numbers expect negative number"
   