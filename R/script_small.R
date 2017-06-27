y = log(data14_7$percent_high)
x = log(data14_7$iterations)
x16 = log(data16_8$iterations)
y16 = log(data16_8$percent_high)
x14 = log(data14_9$iterations)
y14 = log(data14_9$percent_high)

shapiro.test(y)
shapiro.test(x)

cor.test(y,x, method='kendall')

shapiro.test(y14)
shapiro.test(x14)

cor.test(y14,x14, method='kendall')

shapiro.test(y16)
shapiro.test(x16)

cor.test(y16,x16, method='kendall')

y_out = boxplot.stats(y)
x_out = boxplot.stats(x)
summary(lm(y~x))
y_out

# proteins_16_8

plot(analyze2_16_8_erroredit$iterations, analyze2_16_8_erroredit$percent_high)

shapiro.test(x16)
shapiro.test(y16)
y16_out = boxplot.stats(y)$out
x16_out = boxplot.stats(x)$out
y16_out
x16_out
cor.test(y16,x16, method='spearman')
summary(lm(y16~x16))
plot(x16,y16)
abline(lm(y16 ~ x16))
x16
y16


shapiro.test(x14)
shapiro.test(y14)


cor.test(x14,y14, method='pearson')
summary(lm(x14~y14))
plot(x14,y14)
abline(lm(y14 ~ x14))
x14
y14

cor.test(x, y, method='pearson')
plot(x,y)
abline(lm(y14~x14))
install.packages('car')
library(car)
ncvTest(x,y)
ncvTest(lm(y ~ x))

cor.test(analyze2_16_8_erroredit$high_score, analyze2_16_8_erroredit$percent_high, method='spearman')
plot(analyze2_16_8_erroredit$high_score, analyze2_16_8_erroredit$percent_high)
abline(lm(analyze2_16_8_erroredit$percent_high~analyze2_16_8_erroredit$high_score))


plot(x, y, xlim=range(x, x14, x16), ylim=range(y, y14, y16), col ='#1b9e77', xlab="iterations", ylab="% highscore configurations", pch=20) 
points(x14, y14, col='#d95f02', pch=20)
points(x16, y16, col='#7570b3', pch=20) 
abline(lm(y~x), col='#1b9e77', lwd=2)
abline(lm(y14~x14), col='#d95f02', lwd=2)
abline(lm(y16~x16), col='#7570b3', lwd=2)
legend("topright",legend=c("n=14, H=7","n=14, H=9","n=16, H=8"), lwd=c(2.5,2.5,2.5), col=c('#1b9e77','#d95f02','#7570b3'))
