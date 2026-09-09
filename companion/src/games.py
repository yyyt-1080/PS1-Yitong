"""Week 3 classroom models. Synthetic illustrations, not a paper replication."""
import math
import numpy as np

def nash_regret(A, B, x, y):
    """Maximum one-player gain, with row/column payoff matrices in the same orientation."""
    A, B, x, y = map(lambda v: np.asarray(v, dtype=float), (A,B,x,y))
    return max(0., float(np.max(A@y)-x@A@y), float(np.max(x@B)-x@B@y))

def coordination_matrix(safe=5.):
    if not 0 < safe < 8: raise ValueError('safe must be between 0 and 8')
    return np.array([[8.,0.],[7.,float(safe)]])

def logit_ch(tau=1.5, gamma=1.2, safe=5., K=16):
    """Truncated Poisson cognitive hierarchy with logit responses.
    Level 0 is uniform; level k responds to normalized lower-level beliefs.
    Precision is gamma**k. This is NOT a QRE fixed-point or a Nash solver.
    Returns population strategy, level strategies, omitted Poisson mass.
    """
    if not 0 <= tau <= 5 or not 1 <= gamma <= 2 or not 1 <= K <= 32:
        raise ValueError('Use 0<=tau<=5, 1<=gamma<=2, 1<=K<=32')
    A=coordination_matrix(safe)
    weights=np.array([math.exp(-tau)*tau**k/math.factorial(k) for k in range(K+1)])
    strategies=[np.array([.5,.5])]
    for k in range(1,K+1):
        belief=weights[:k] @ np.array(strategies) / weights[:k].sum()
        z=(gamma**k)*(A@belief); z-=z.max()
        response=np.exp(z); strategies.append(response/response.sum())
    levels=np.array(strategies)
    population=(weights/weights.sum())@levels
    return population,levels,max(0.,float(1-weights.sum()))

def entry_spne(fight=(-1.,-1.), accommodate=(1.,1.), out=(0.,2.)):
    """Return all backward-induction outcomes, preserving ties."""
    cont={'Fight':fight,'Accommodate':accommodate}; best=max(v[1] for v in cont.values()); result=[]
    for action,payoff in cont.items():
        if payoff[1] != best: continue
        entrant_best=max(out[0],payoff[0])
        for initial,p in [('Out',out),('In',payoff)]:
            if p[0]==entrant_best: result.append((initial,action,p))
    return result
