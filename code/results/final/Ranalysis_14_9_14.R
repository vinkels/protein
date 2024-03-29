iterations = ana14_9$Iterations
outside = ana14_9$absoutside
ratio = ana14_9$absoddeven
SAperc = ana14_9$percentSA
shapiro.test(iterations)

#niet significant
cor.test(iterations, outside, method="kendall")
#significant p-value = 0.0002762, tau = -0.29874
cor.test(iterations, ratio, method = "kendall")

#niet significant
cor.test(SAperc, outside, method = "kendall")
# significant (p-value = 0.001554, 0.2837454)
cor.test(SAperc, ratio, method = "kendall")

plot(SAperc, iterations)
plot(ratio, iterations)
