"""Basic checks for the chatbot response function."""

import unittest

from chatbot import get_response


class GetResponseTests(unittest.TestCase):
    def test_known_messages(self):
        self.assertEqual(get_response("hello"), "Hi! How can I help you?")
        self.assertEqual(get_response("HI"), "Hi! How can I help you?")
        self.assertEqual(get_response(" how are you "), "I'm fine, thanks!")
        self.assertEqual(get_response("bye"), "Goodbye!")

    def test_unknown_message(self):
        self.assertEqual(
            get_response("what is your name"),
            "Sorry, I don't understand that.",
        )


if __name__ == "__main__":
    unittest.main()
