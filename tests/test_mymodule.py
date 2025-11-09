from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import unittest
import utils.mymodule as mymodule

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = f'{protocol}://{host}.{domain}\n'
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)
            

if __name__ == '__main__':
    unittest.main()