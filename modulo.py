# Modulo is really common in a particular pattern with for and if. Here's an example:
for n in range(12):
   if n % 3 == 0:
      draw_triangle()
   else:
      draw_square()

 #   In other words, this is the same as 

draw_triangle()
draw_square()
draw_square()

draw_triangle()
draw_square()
draw_square()

draw_triangle()
draw_square()
draw_square()

draw_triangle()
draw_square()
draw_square()