import unittest
import models.trip


class MyTestCase(unittest.TestCase):
    def test_next_train(self):
        t1 = models.trip.Trip.next_trains("GARE DE PARIS AUSTERLITZ")
        print("t1:", t1)
        t2 = models.trip.Trip.next_trains("SAINTE-GENEVIEVE DES BOIS", "GARE DE PARIS AUSTERLITZ")
        self.assertTrue(t1 is not None)
        self.assertTrue(t2 is not None)


if __name__ == '__main__':
    unittest.main()
