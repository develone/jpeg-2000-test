from myhdl import *
WIDTH_OUT = 36
WIDTH = 31
W0 = 9
upd0 = Signal(bool(0))
upd1 = Signal(bool(0))
z0 = Signal(intbv(0)[W0:])
z1 = Signal(intbv(0)[W0:])
done0 = Signal(bool(0))
done1 = Signal(bool(0))
res0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs0 = Signal(intbv(0)[3:])
flgs1 = Signal(intbv(0)[3:])
lft0 = Signal(intbv(0)[W0:])
lft1 = Signal(intbv(0)[W0:])
sam0 = Signal(intbv(0)[W0:])
sam1 = Signal(intbv(0)[W0:])
rht0 = Signal(intbv(0)[W0:])
rht1 = Signal(intbv(0)[W0:])
lift0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

upd2 = Signal(bool(0))
upd3 = Signal(bool(0))
z2 = Signal(intbv(0)[W0:])
z3 = Signal(intbv(0)[W0:])
done2 = Signal(bool(0))
done3 = Signal(bool(0))
res2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs2 = Signal(intbv(0)[3:])
flgs3 = Signal(intbv(0)[3:])
lft2 = Signal(intbv(0)[W0:])
lft3 = Signal(intbv(0)[W0:])
sam2 = Signal(intbv(0)[W0:])
sam3 = Signal(intbv(0)[W0:])
rht2 = Signal(intbv(0)[W0:])
rht3 = Signal(intbv(0)[W0:])
lift2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

upd4 = Signal(bool(0))
upd5 = Signal(bool(0))
z4 = Signal(intbv(0)[W0:])
z5 = Signal(intbv(0)[W0:])
done4 = Signal(bool(0))
done5 = Signal(bool(0))
res4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs4 = Signal(intbv(0)[3:])
flgs5 = Signal(intbv(0)[3:])
lft4 = Signal(intbv(0)[W0:])
lft5 = Signal(intbv(0)[W0:])
sam4 = Signal(intbv(0)[W0:])
sam5 = Signal(intbv(0)[W0:])
rht4 = Signal(intbv(0)[W0:])
rht5 = Signal(intbv(0)[W0:])
lift4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

upd6 = Signal(bool(0))
upd7 = Signal(bool(0))
z6 = Signal(intbv(0)[W0:])
z7 = Signal(intbv(0)[W0:])
done6 = Signal(bool(0))
done7 = Signal(bool(0))
res6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs6 = Signal(intbv(0)[3:])
flgs7 = Signal(intbv(0)[3:])
lft6 = Signal(intbv(0)[W0:])
lft7 = Signal(intbv(0)[W0:])
sam6 = Signal(intbv(0)[W0:])
sam7 = Signal(intbv(0)[W0:])
rht6 = Signal(intbv(0)[W0:])
rht7 = Signal(intbv(0)[W0:])
lift6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))


myregister0 = Signal(intbv(0)[32:])
myregister1 = Signal(intbv(0)[32:])
myregister2 = Signal(intbv(0)[32:])
myregister3 = Signal(intbv(0)[32:])
myregister4 = Signal(intbv(0)[32:])
myregister5 = Signal(intbv(0)[32:])
myregister6 = Signal(intbv(0)[32:])
myregister7 = Signal(intbv(0)[32:])
 
data_to_host0 = Signal(intbv(0)[32:])
data_to_host1 = Signal(intbv(0)[32:])
data_to_host2 = Signal(intbv(0)[32:])
data_to_host3 = Signal(intbv(0)[32:])
