iterations = ana14_7$iterations
outside = ana14_7$absoutside
ratio = ana14_7$absoddeven
rratio= ana14_7$oddeven
SAperc = ana14_7$percentage
shapiro.test(iterations)

#niet significant
cor.test(iterations, outside, method="kendall")
#niet significant (p=0.05)
cor.test(iterations, ratio, method = "kendall")

#niet significant
cor.test(SAperc, outside, method = "kendall")
#niet significant
cor.test(SAperc, ratio, method = "kendall")

plot(SAperc, iterations)
plot(rratio, iterations)
