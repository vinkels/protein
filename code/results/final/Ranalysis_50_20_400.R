iteration = X50buckets$total_iteration
shapiro.test(iteration)

out = X50buckets$outside
plot(out, iteration)
middle = X50buckets$middle
plot(middle, iteration)
left = X50buckets$left
plot(left, iteration)
right = X50buckets$right
plot(right, iteration)
bucket1 = X50buckets$side_1
plot(bucket1, iteration)
bucket2 = X50buckets$side_2
plot(bucket2, iteration)
bucket3 = X50buckets$side_3
plot(bucket3, iteration)
bucket4 = X50buckets$side_4
plot(bucket4, iteration)
outin = XX50buckets$outeveninodd
plot(outin, iteration)
ratio = XX50buckets$abs_ratio
plot(ratio, iteration)

# significant (p = 0.022, tau = -0.1684452)
cor.test(out, iteration, method="kendall")
#niet significant
cor.test(middle, iteration, method="kendall")
#niet significant
cor.test(left, iteration, method="kendall")
#niet significant
cor.test(right, iteration, method="kendall")
#niet significant
cor.test(bucket1, iteration, method ="kendall")
#niet significant
cor.test(bucket2, iteration, method ="kendall")
#niet significant
cor.test(bucket3, iteration, method ="kendall")
#niet significant
cor.test(bucket4, iteration, method ="kendall")
#niet significant (p=0.08)
cor.test(outin, iteration, method ="kendall")
#SIGNIFICANT!!! p=0.02687,tau= -0.1733199 
cor.test(ratio, iteration, method="kendall")
