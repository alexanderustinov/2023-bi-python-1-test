from main import tr, f

eps = 0.001


def test():
    a=0
    b=1
    n=151
    assert abs(tr(a,b,n+1)- tr(a,b,n))<eps, f"Точность {eps} не достигнута"
