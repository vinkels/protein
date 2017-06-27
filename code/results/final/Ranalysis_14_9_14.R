iterations = ana14_9$Iterations
outside = ana14_9$absoutside
ratio = ana14_9$absoddeven

shapiro.test(iterations)

cor.test(iterations, out)