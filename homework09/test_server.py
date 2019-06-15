import requests
import unittest
import socket


class TestAsyncHTTPServer(unittest.TestCase):
    host = "http://localhost"
    port = 9000

    def setUp(self):
        pass

    def test_empty_request(self):
        """Send empty request"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", self.port))
        s.sendall(b"\n")
        s.close()

    def test_server_header(self):
        """Server header exists"""
        r = requests.get(f'{self.host}:{self.port}')
        server = r.headers.get('Server')
        self.assertIsNotNone(server)

    def test_date_header(self):
        """Date header exists"""
        r = requests.get(f'{self.host}:{self.port}')
        date = r.headers.get('Date')
        self.assertIsNotNone(date)

    def test_directory_index(self):
        """Directory index file exists"""
        r = requests.get(f'{self.host}:{self.port}')
        data = r.content.decode()
        length = r.headers.get('Content-Length')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 34)
        self.assertEqual(len(data), 34)
        self.assertEqual(data, "<html>Directory index file</html>\n")

    def test_index_not_found(self):
        """Directory index file absent"""
        r = requests.get(f'{self.host}:{self.port}/1')
        self.assertEqual(int(r.status_code), 404)

    def test_file_in_nested_folders(self):
        """File located in nested folders"""
        r = requests.get(f'{self.host}:{self.port}/files/holder/text.txt')
        data = r.content
        length = r.headers.get('Content-Length')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 6)
        self.assertEqual(len(data), 6)
        self.assertEqual(data.decode(), '123 Hi')

    def test_file_with_query_string(self):
        """Slash after filename"""
        r = requests.get(f'{self.host}:{self.port}/404/index.html/')
        self.assertEqual(r.status_code, 404)

    def test_file_with_query_string(self):
        """Query string after filename"""
        r = requests.get(f'{self.host}:{self.port}/files/index.html?arg1=value&arg2=value')
        data = r.content
        length = r.headers.get('Content-Length')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 38)
        self.assertEqual(len(data), 38)
        self.assertEqual(data.decode(), '<html><body>Page sample</body></html>\n')

    def test_file_with_dot_in_name(self):
        """File with two dots in name"""
        r = requests.get(f'{self.host}:{self.port}/files/text..txt')
        data = r.content.decode()
        length = r.headers.get('Content-Length')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 6)
        self.assertEqual(len(data), 6)
        self.assertIn('123 Hi', data)

    def test_post_method(self):
        """Post method forbidden"""
        r = requests.post(f'{self.host}:{self.port}/files/index.html')
        self.assertIn(int(r.status_code), (400, 405))

    def test_head_method(self):
        """Head method support"""
        r = requests.head(f'{self.host}:{self.port}/files/index.html')
        data = r.content.decode()
        length = r.headers.get('Content-Length')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 38)
        self.assertEqual(len(data), 0)

    def test_filetype_html(self):
        """Content-Type for .html"""
        r = requests.get(f'{self.host}:{self.port}/files/index.html')
        data = r.content
        length = r.headers.get('Content-Length')
        ctype = r.headers.get('Content-Type')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 38)
        self.assertEqual(len(data), 38)
        self.assertEqual(ctype, "text/html")

    def test_filetype_css(self):
        """Content-Type for .css"""
        r = requests.get(f'{self.host}:{self.port}/files/main.css')
        data = r.content
        length = r.headers.get('Content-Length')
        ctype = r.headers.get('Content-Type')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 6830)
        self.assertEqual(len(data), 6830)
        self.assertEqual(ctype, "text/css")

    def test_filetype_jpg(self):
        """Content-Type for .jpg"""
        r = requests.get(f'{self.host}:{self.port}/files/dog.jpg')
        data = r.content
        length = r.headers.get('Content-Length')
        ctype = r.headers.get('Content-Type')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 196302)
        self.assertEqual(len(data), 196302)
        self.assertEqual(ctype, "image/jpeg")

    def test_filetype_jpeg(self):
        """Content-Type for .jpeg"""
        r = requests.get(f'{self.host}:{self.port}/files/messi.jpeg')
        data = r.content
        length = r.headers.get('Content-Length')
        ctype = r.headers.get('Content-Type')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 53034)
        self.assertEqual(len(data), 53034)
        self.assertEqual(ctype, "image/jpeg")

    def test_filetype_png(self):
        """Content-Type for .png"""
        r = requests.get(f'{self.host}:{self.port}/files/gomer.png')
        data = r.content
        length = r.headers.get('Content-Length')
        ctype = r.headers.get('Content-Type')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(int(length), 137452)
        self.assertEqual(len(data), 137452)
        self.assertEqual(ctype, "image/png")

loader = unittest.TestLoader()
suite = unittest.TestSuite()
a = loader.loadTestsFromTestCase(TestAsyncHTTPServer)
suite.addTest(a)


class NewResult(unittest.TextTestResult):
    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        return doc_first_line or ""


class NewRunner(unittest.TextTestRunner):
    resultclass = NewResult


runner = NewRunner(verbosity=2)
runner.run(suite)
