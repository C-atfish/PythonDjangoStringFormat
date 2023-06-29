import logging
import math
import re


class Wrapper:
    @staticmethod
    def wrap(input_string, cut_off_number):

        # Split the whole string by spaces and dashes
        split_string = re.split('-|\s', input_string)

        result = ""
        # loop through every word, to check if it needs to be split or not
        for word in split_string:

            # If word in longer than cutoff, should split word, keeps splitting on long words until there is nothing left
            # Appends new line after every correct word
            if len(word) > cut_off_number:
                while len(word) > cut_off_number:
                    split_word = word[:cut_off_number]
                    split_word += "\n"
                    result += split_word

                    word = word[cut_off_number:]

                if word:
                    word += "\n"
                    result += word

            else:
                word += "\n"
                result += word

        return result
