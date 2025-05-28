# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(expon.cdf(4, scale=2.5))

# Print probability response takes > 4 hours
probability_less_than_4 = expon.cdf(4, scale=2.5)
probability_more_than_4 = 1 - probability_less_than_4
print(probability_more_than_4)

# Print probability response takes 3-4 hours
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))
