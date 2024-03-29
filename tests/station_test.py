import unittest
import models.station


class MyTestCase(unittest.TestCase):
    def test_get_stations(self):
        self.assertTrue(models.station.Station.get_stations() is not None)

    def test_find_station(self):
        s1 = models.station.Station.find_station("GARE DE PARIS AUSTERLITZ")
        s2 = models.station.Station.find_station("GARE D'AUSTERLITZ")
        s3 = models.station.Station.find_station("GARE DE LOS ANGELES")
        self.assertTrue(s1 is not None)
        self.assertTrue(s2 is not None)
        self.assertTrue(s3 is None)

    def test_compare_station(self):
        s1 = models.station.Station.find_station("GARE DE PARIS AUSTERLITZ")
        s2 = models.station.Station.find_station("GARE D'AUSTERLITZ")
        s3 = models.station.Station.find_station("GARE DE LOS ANGELES")
        self.assertTrue(s1 == s2)
        self.assertTrue(s1 != s3)

    def test_search_places(self):
        s1 = models.station.Station.search_list_places("austerlitz")
        s2 = models.station.Station.search_list_places("dourdan la foret", models.station.PlaceType.tramway)
        self.assertTrue(len(s1) != 0)
        self.assertTrue(len(s2) == 0)


if __name__ == '__main__':
    unittest.main()
