
print()
var1 = int(input("Input var1 value: "));
var2 = int(input("Input var2 value: "));
incr = int(input("Input increment: "));

def while_loop_fn(var1, var2, incr):
    i = 0
    while var1 < 50:
        print ("While Loop Iteration {0:2d}: var1 = {1:3d}, var2 = {2:3d}".format(i, var1, var2))
        var1 += 5 * incr
        var2 += 6 * incr
        i += incr

    print("The while loop is done\n")


def for_loop_fn(var1, var2, incr):
    i = 0
    for var1 in range (5, 50, 5):
        print ("For Loop Iteration {0:2d}: var1 = {1:3d}, var2 = {2:3d}".format(i, var1, var2))
        var1 += 5 * incr
        var2 += 6 * incr
        i += incr

    print("The for loop is done\n")

while_loop_fn(var1, var2, incr)
for_loop_fn(var1, var2, incr)
