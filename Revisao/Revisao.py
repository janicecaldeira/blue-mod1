import turtle


print("-~-.-~-.-~-."* 10)
print("SUPER MARIO AO RESGATE".center(120))
print("-~-.-~-.-~-." * 10)




color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
