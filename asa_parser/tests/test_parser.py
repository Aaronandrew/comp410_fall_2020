import unittest
import asa_parser as ap


class ParserTest(unittest.TestCase):
    def test_show_clock(self):
        # This is the expected value
        expected = '{"timestamp": ["12:40:33.800 UTC Wed Aug 16 2017"]}'

        # Check to make sure the parser returns the expected value
        asa = ap.AsaParser('show_clock.txt')
        self.assertEqual(expected, asa.clock())

    def test_show_failover_history(self):
        # This is the expected value
        expected = '[{"group": "0", "timestamp": "16:43:08 UTC Aug 8 2017", "FromState": "Active Applying Config", ' \
                   '"ToState": "Active Config Applied", "Reason": "No Active unit found"}, {"group": "0", ' \
                   '"timestamp": "16:43:08 UTC Aug 8 2017", "FromState": "Active Config Applied", "ToState": ' \
                   '"Active", "Reason": "No Active unit found"}, {"group": "1", "timestamp": "16:43:09 UTC Aug 8 ' \
                   '2017", "FromState": "Negotiation", "ToState": "Just Active", "Reason": "No Active unit found"}, ' \
                   '{"group": "2", "timestamp": "16:43:09 UTC Aug 8 2017", "FromState": "Disabled", "ToState": ' \
                   '"Negotiation", "Reason": "Failover state check"}, {"group": "1", "timestamp": "16:43:10 UTC Aug 8 ' \
                   '2017", "FromState": "Just Active", "ToState": "Active Drain", "Reason": "No Active unit found"}, ' \
                   '{"group": "1", "timestamp": "16:43:10 UTC Aug 8 2017", "FromState": "Active Drain", "ToState": ' \
                   '"Active Applying Config", "Reason": "No Active unit found"}, {"group": "1", "timestamp": ' \
                   '"16:43:10 UTC Aug 8 2017", "FromState": "Active Applying Config", "ToState": "Active Config ' \
                   'Applied", "Reason": "No Active unit found"}, {"group": "1", "timestamp": "16:43:10 UTC Aug 8 ' \
                   '2017", "FromState": "Active Config Applied", "ToState": "Active", "Reason": "No Active unit ' \
                   'found"}, {"group": "2", "timestamp": "16:43:11 UTC Aug 8 2017", "FromState": "Negotiation", ' \
                   '"ToState": "Just Active", "Reason": "No Active unit found"}, {"group": "2", "timestamp": ' \
                   '"16:43:11 UTC Aug 8 2017", "FromState": "Just Active", "ToState": "Active Drain", "Reason": "No ' \
                   'Active unit found"}, {"group": "2", "timestamp": "16:43:11 UTC Aug 8 2017", "FromState": "Active ' \
                   'Drain", "ToState": "Active Applying Config", "Reason": "No Active unit found"}, {"group": "2", ' \
                   '"timestamp": "16:43:11 UTC Aug 8 2017", "FromState": "Active Applying Config", "ToState": "Active ' \
                   'Config Applied", "Reason": "No Active unit found"}, {"group": "2", "timestamp": "16:43:11 UTC Aug ' \
                   '8 2017", "FromState": "Active Config Applied", "ToState": "Active", "Reason": "No Active unit ' \
                   'found"}, {"group": "2", "timestamp": "17:37:12 UTC Aug 8 2017", "FromState": "Active", ' \
                   '"ToState": "Standby Ready", "Reason": "Other unit wants me Standby"}, {"group": "2", "timestamp": ' \
                   '"14:01:14 UTC Aug 16 2017", "FromState": "Standby Ready", "ToState": "Just Active", ' \
                   '"Reason": "HELLO not heard from mate"}, {"group": "2", "timestamp": "14:01:15 UTC Aug 16 2017", ' \
                   '"FromState": "Just Active", "ToState": "Active Drain", "Reason": "HELLO not heard from mate"}, ' \
                   '{"group": "2", "timestamp": "14:01:15 UTC Aug 16 2017", "FromState": "Active Drain", "ToState": ' \
                   '"Active Applying Config", "Reason": "HELLO not heard from mate"}, {"group": "2", "timestamp": ' \
                   '"14:01:15 UTC Aug 16 2017", "FromState": "Active Applying Config", "ToState": "Active Config ' \
                   'Applied", "Reason": "HELLO not heard from mate"}, {"group": "2", "timestamp": "14:01:15 UTC Aug ' \
                   '16 2017", "FromState": "Active Config Applied", "ToState": "Active", "Reason": "HELLO not heard ' \
                   'from mate"}, {"group": "2", "timestamp": "15:27:30 UTC Aug 16 2017", "FromState": "Active", ' \
                   '"ToState": "Standby Ready", "Reason": "Other unit wants me Standby"}]'

        # Check to make sure the parser returns the expected value
        asa = ap.AsaParser('show_failover_history.txt')
        self.assertEqual(expected, asa.failover_history())
