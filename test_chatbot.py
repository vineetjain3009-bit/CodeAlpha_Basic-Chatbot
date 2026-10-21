"""Basic checks for the chatbot response function."""

import unittest

from chatbot import get_response, should_exit


class GetResponseTests(unittest.TestCase):
    def test_known_messages(self):
        self.assertEqual(get_response("hello"), "Hi! How can I help you?")
        self.assertEqual(get_response("Hello chatbot"), "Hi! How can I help you?")
        self.assertEqual(get_response("HI"), "Hi! How can I help you?")
        self.assertEqual(get_response(" how are you "), "I'm fine, thanks!")
        self.assertEqual(
            get_response("What is your name?"),
            "I'm a simple rule-based chatbot.",
        )
        self.assertEqual(get_response("thank you"), "You're welcome!")
        self.assertEqual(
            get_response("help"),
            "I can respond to greetings and a few basic conversation questions.",
        )
        self.assertEqual(get_response("bye"), "Goodbye!")

    def test_exit_messages(self):
        self.assertTrue(should_exit(" bye "))
        self.assertTrue(should_exit("QUIT!"))
        self.assertFalse(should_exit("hello"))

    def test_unknown_message(self):
        self.assertEqual(
            get_response("what is the weather today"),
            "Sorry, I don't understand that.",
        )


if __name__ == "__main__":
    unittest.main()
