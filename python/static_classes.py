class X(object):
    x = "name"

    @staticmethod
    def p():
        print(X.x)

    @staticmethod
    def ins(aa):
        X.x += aa


X.p()
X.ins(" aaaa")
X.p()
