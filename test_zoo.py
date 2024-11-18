import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "false")
       
    # Add your additional test cases here.
    def test_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)

    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_child_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_child_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(80), 100)
        
if __name__ == '__main__':
    unittest.main()