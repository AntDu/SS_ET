from unittest import TestCase

from Analysis_of_envelopes import Envelope
from Analysis_of_envelopes import envelope_analysis


class TestEnvelopeEntry(TestCase):

    def test_envelope_second_fit_in_first(self):

        envelope1 = Envelope(7, 9)
        envelope2 = Envelope(5, 4)
        result = envelope_analysis(envelope1, envelope2)
        self.assertEqual(result, 'Second envelope fit in First\n')

    def test_envelope_first_fit_in_Second(self):

        envelope1 = Envelope(5, 4)
        envelope2 = Envelope(7, 9)
        result = envelope_analysis(envelope1, envelope2)
        self.assertEqual(result, 'First envelope fit in Second\n')

    def test_envelope_same_envelopes(self):

        envelope1 = Envelope(6, 8)
        envelope2 = Envelope(8, 6)
        result = envelope_analysis(envelope1, envelope2)
        self.assertEqual(result, 'The same envelopes.\n')


if __name__ == '__main__':
    TestEnvelopeEntry()