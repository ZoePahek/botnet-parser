import unittest
from src import botnet_parser


class TestParser(unittest.TestCase):

    # Only created test cases for file parsing, since the online data changes and would not produce the same results
    # when parsed at varying times
    def setUp(self):
        self.file_path1 = '../test_data/dircrypt-master.csv'
        self.file_path2 = '../test_data/bedep-master.csv'
        self.file_path3 = '../test_data/bamital-master.csv'
        self.file_path4 = '../test_data/simda-master.csv'

        # Creates a testing instance off of the first file path
        self.parser1 = botnet_parser.BotnetParser()
        self.parser1._master_data_from_file(self.file_path1)

        # Creates a testing instance off of the second file path
        self.parser2 = botnet_parser.BotnetParser()
        self.parser2._master_data_from_file(self.file_path2)

        # Creates a testing instance off of the third file path
        self.parser3 = botnet_parser.BotnetParser()
        self.parser3._master_data_from_file(self.file_path3)

        self.parser4 = botnet_parser.BotnetParser()
        self.parser4._master_data_from_file(self.file_path4)

    def test_correct_domains(self):
        correct_domains1 = {'kcubcfuhwwn.com', 'lscyqrjofqmtn.com', 'lxpcmncky.com', 'ojglbpuhj.com',
                            'pihxsxitdfzpvpgeusf.com', 'plxeyaja.com', 'sjytgtnkdl.com', 'vjuxtixi.com',
                            'zpjjtxthazjghwvdlzy.com'}
        correct_domains2 = {'afapudcvknpewfc.com', 'dbmcyuvozctlkdcic.com', 'ddspecysoheir.com',
                            'dkduxfjkodu6.com', 'mfzufqcvbfdx.com', 'nnlinvfzkc3g.com', 'pfofzbmhseg95.com',
                            'rfcalswtyxok.com', 'sdbzkydkadlpmrj.com', 'wajfzyrronaxg5.com',
                            'xtyrxbnxsnxsvwh0.com', 'yulqqmaciqzskzm.com'}
        correct_domains3 = set()
        self.assertEqual(correct_domains1, self.parser1.domains,
                         msg='Parser should have {} as its set of domains but instead has {}.'.format(
                             correct_domains1, self.parser1.domains))
        self.assertEqual(correct_domains2, self.parser2.domains,
                         msg='Parser should have {} as its set of domains but instead has {}.'.format(
                             correct_domains2, self.parser2.domains))
        self.assertEqual(correct_domains3, self.parser3.domains,
                         msg='Parser should have {} as its set of domains but instead has {}.'.format(
                             correct_domains3, self.parser3.domains))

    def test_correct_ips(self):
        correct_ips1 = ['169.50.13.61', '164.155.204.36', '193.146.253.35']
        correct_ips2 = ['173.231.184.117', '52.0.217.44', '162.217.99.136', '173.231.184.57', '72.26.218.84',
                        '72.26.218.74', '72.251.233.252', '107.6.74.79']
        correct_ips3 = []
        correct_ips4 = ['193.41.64.176', '141.105.126.87']  # Only uses the first and last IP
        self.assertEqual(correct_ips1, self.parser1.ips,
                         msg='Parser should have {} as its list of ips but instead has {}.'.format(
                             correct_ips1, self.parser1.ips))
        self.assertEqual(correct_ips2, self.parser2.ips,
                         msg='Parser should have {} as its list of ips but instead has {}.'.format(
                             correct_ips2, self.parser2.ips))
        self.assertEqual(correct_ips3, self.parser3.ips,
                         msg='Parser should have {} as its list of ips but instead has {}.'.format(
                             correct_ips3, self.parser3.ips))
        self.assertEqual(correct_ips4[0], self.parser4.ips[0], msg='The first IP in parser is incorrect')
        self.assertEqual(correct_ips4[-1], self.parser4.ips[-1], msg='The last IP in parser is incorrect')

    def test_correct_repeating_ips(self):
        correct_repeating_ips1 = {'169.50.13.61': 4, '193.146.253.35': 4}
        correct_repeating_ips2 = {'52.0.217.44': 4, '162.217.99.136': 2}
        correct_repeating_ips3 = {}
        self.assertEqual(correct_repeating_ips1, self.parser1.repeating_ips_count,
                         msg='Parser should have {} as its set of repeating ips but instead has {}.'.format(
                             correct_repeating_ips1, self.parser1.repeating_ips_count))
        self.assertEqual(correct_repeating_ips2, self.parser2.repeating_ips_count,
                         msg='Parser should have {} as its set of repeating ips but instead has {}.'.format(
                             correct_repeating_ips2, self.parser2.repeating_ips_count))
        self.assertEqual(correct_repeating_ips3, self.parser3.repeating_ips_count,
                         msg='Parser should have {} as its set of repeating ips but instead has {}.'.format(
                             correct_repeating_ips3, self.parser3.repeating_ips_count))

    def test_correct_multiple_ip_uses1(self):
        correct_multiple_ip_uses1 = {}
        correct_multiple_ip_uses3 = {}
        self.parser1.find_similar_dns_info()
        self.assertEqual(correct_multiple_ip_uses1, self.parser1.multiple_ip_uses,
                         msg='Parser should have {} as the dictionary for multiple_pointers, '
                             'but instead has {}.'.format(correct_multiple_ip_uses1,
                                                          self.parser1.multiple_ip_uses))
        self.parser3.find_similar_dns_info()
        self.assertEqual(correct_multiple_ip_uses3, self.parser3.multiple_ip_uses,
                         msg='Parser should have {} as the dictionary for multiple_pointers, '
                             'but instead has {}.'.format(correct_multiple_ip_uses3,
                                                          self.parser3.multiple_ip_uses))

    def test_correct_multiple_ip_uses2(self):
        # Since the lists for this test case were longer than others, I only created tests for two keys
        correct_multiple_ip_uses2 = {'54.221.105.86': {'173.231.184.117', '162.217.99.136', '173.231.184.57',
                                                       '72.26.218.84', '72.26.218.74', '72.26.218.74',
                                                       '72.251.233.252', '107.6.74.79'},
                                     '3.87.22.163': {'162.217.99.136', '173.231.184.57', '72.26.218.84',
                                                     '107.6.74.79'}}
        correct_multiple_ip_uses4 = {'195.206.121.10': {'46.30.215.194', '77.111.240.32', '77.111.240.52',
                                                        '91.212.28.29', '46.30.215.126'},
                                     '81.2.216.125': {'62.149.128.151', '62.149.128.154', '62.149.128.157',
                                                      '62.149.128.160', '62.149.128.163', '62.149.128.166',
                                                      '62.149.128.72', '62.149.128.74', '89.46.108.57',
                                                      '31.11.32.144'}}
        self.parser2.find_similar_dns_info()
        keys = correct_multiple_ip_uses2.keys()
        for key in keys:
            self.assertTrue(self.parser2.multiple_ip_uses[key])  # Tests if the correct keys exist in the dictionary
            self.assertEqual(correct_multiple_ip_uses2[key], self.parser2.multiple_ip_uses[key])
        self.parser4.find_similar_dns_info()
        keys = correct_multiple_ip_uses4.keys()
        for key in keys:
            self.assertTrue(self.parser4.multiple_ip_uses[key])  # Tests if the correct keys exist in the dictionary
            self.assertEqual(correct_multiple_ip_uses4[key], self.parser4.multiple_ip_uses[key])

    def test_correct_multiple_host_uses(self):
        correct_multiple_host_uses = {'ns01.one.com': {'46.30.215.194', '77.111.240.32', '77.111.240.52',
                                                       '91.212.28.29', '46.30.215.126'},
                                      'dns2.technorail.com': {'62.149.128.151', '62.149.128.154', '62.149.128.157',
                                                              '62.149.128.160', '62.149.128.163', '62.149.128.166',
                                                              '62.149.128.72', '62.149.128.74', '89.46.108.57',
                                                              '31.11.32.144'}}
        self.parser4.find_similar_dns_info()
        keys = correct_multiple_host_uses.keys()
        for key in keys:
            self.assertTrue(self.parser4.multiple_host_uses[key])  # Tests if the correct keys exist in the dictionary
            self.assertEqual(correct_multiple_host_uses[key], self.parser4.multiple_host_uses[key])

    def test_correct_locations(self):
        correct_locations1 = {'US': 2, 'ES': 1}
        correct_locations2 = {'US': 6, 'NL': 2}
        correct_locations3 = {}
        self.parser1.find_countries()
        self.assertEqual(correct_locations1, self.parser1.countries)

        self.parser2.find_countries()
        self.assertEqual(correct_locations2, self.parser2.countries)

        self.parser3.find_countries()
        self.assertEqual(correct_locations3, self.parser3.countries)


if __name__ == '__main__':
    unittest.main()
