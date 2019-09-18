import numpy as np

from scipy.stats import norm
from scipy.stats import bernoulli

class rowexp_new_batch:

    def __init__(self, NUMHYP, numdraws, alt_vec, mu0, mu_alt_vec):
        self.numhyp = NUMHYP
        self.alt_vec = alt_vec
        self.mu0 = mu0
        self.mu_vec = mu0*np.ones(NUMHYP) + np.multiply(alt_vec, mu_alt_vec)
        self.pvec = np.zeros(NUMHYP)
        self.numdraws = numdraws

        '''
        Function drawing p-values: Mixture of two Gaussians
        '''
    def gauss_two_mix(self, mu_gap, sigma = 1, rndsd = 0):

        np.random.seed(rndsd)

        # Draw Z values according to lag
        Z = self.mu_vec + np.random.randn(self.numhyp)*sigma # draw gaussian acc. to hypothesis, if sigma are all same


        # Compute p-values and save
        if mu_gap > 0:
            self.pvec = [(1 - norm.cdf(z)) for z in Z] # one-sided p-values
        else:
            self.pvec = [2*norm.cdf(-abs(z)) for z in Z] # two-sided p-values

    def beta_draws(self, rndsd = 0):
        np.random.seed(rndsd)
        self.pvec = [(np.random.beta(0.5,5,1)*self.alt_vec[i]+np.random.uniform(0,1,1)*(1-self.alt_vec[i])) for i in range(self.numhyp)]
