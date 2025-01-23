import taichi as ti
import taichi.math as tm

ti.init(arch=ti.gpu)

@ti.kernel
def test():
    x = 1
    x = 3.14
