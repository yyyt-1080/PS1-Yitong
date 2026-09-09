import unittest
import numpy as np
from src.games import *
class Models(unittest.TestCase):
 def test_known_nash(self):
  A=coordination_matrix();B=A.T
  for p in [0.,1.,5/6]: self.assertLess(nash_regret(A,B,[p,1-p],[p,1-p]),1e-9)
 def test_out_of_equilibrium(self):
  A=coordination_matrix();self.assertGreater(nash_regret(A,A.T,[.5,.5],[.5,.5]),.1)
 def test_entry(self):self.assertEqual(entry_spne()[0][:2],('In','Accommodate'))
 def test_ch_limits(self):
  p,_,_=logit_ch(tau=0);np.testing.assert_allclose(p,[.5,.5])
  for tau in [0,1.5,5]:
   p,levels,tail=logit_ch(tau=tau);self.assertAlmostEqual(p.sum(),1);self.assertTrue(np.all(p>=0));self.assertLess(tail,1e-4)
 def test_truncation(self):np.testing.assert_allclose(logit_ch(5,K=16)[0],logit_ch(5,K=24)[0],atol=1e-4)
if __name__=='__main__':unittest.main()
