"""n2w: number to word conversion model: contain function
    num2words. Can also be run as a script
usage as a script: n2w num
        (Convert a number to its English word description)
        num: whole integer from 0 to 999,999,999,999,999(comma are
        option)
example: n2w 10,003,103
        for 10,003,103 say: ten million three thousand one hundred three
"""
import sys, string, argparse
_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
            '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen',
                '5': 'fifteen', '6': 'sixteen', '7': 'seventeen', '8': 'eighteen',
                '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'fourty', '5': 'fifty', '6': 'sixty',
                '7': 'seventy', '8': 'eighty', '9': 'ninety'}
# 量级列表：每3位就会提升一个量级，从空('')到千('thousand')，百万('million'),十亿('billion'),万亿('trillion')
_magnitude_list = [(0, ''), (3, ' thousand '), (6, ' million '), (9, ' billion '),
                (12, ' trillion '), (15, '')]
def num2words(num_string):
        """num2words(num_string): convert number to English words"""
        if num_string == '0':
                return 'zero'
        max_len = _magnitude_list[-1][0]
        num_string = num_string.replace(",", "") # 去除","号
        num_len = len(num_string)
        if num_len > max_len:
                return "Sorry, can't handle numbers with more than" \
                        "{0} digits".format(max_len)
        word_string = ''
        num_string = '00' + num_string
        for length, magnitude in _magnitude_list:
                if length >= num_len:
                        return word_string
                else:
                        hundreds = num_string[-length - 3]
                        tens = num_string[-length - 2]
                        ones = num_string[-length - 1]
                        if not (hundreds == tens == ones == '0'):
                                word_string = _handleto999(hundreds, tens, ones) + magnitude + \
                                        word_string
def _handleto999(hundreds, tens, ones):
        word_string = ''
        if not(hundreds == '0'):
                word_string += _1to9dict[hundreds] + " hundred "
        if not(tens == '0'):
                if tens == '1':
                        word_string += _10to19dict[ones]
                        return word_string
                elif tens == '0':
                        pass
                else:
                        word_string += _20to90dict[tens] + ' '
        if not(ones == '0'):
                word_string += _1to9dict[ones]
        return word_string
def test():
        values = sys.stdin.read().split()
        for val in values:
                print("{0} = {1}".format(val, num2words(val)))
def main():
        parser = argparse.ArgumentParser(usage=__doc__)
        parser.add_argument("num", nargs='*')
        parser.add_argument("-t", "--test", dest="test",
                        action='store_true' ,default=False,
                        help="Test mode: reads from stdin")
        args = parser.parse_args()
        if args.test:
                test()
        else:
                try:
                        result = num2words(args.num[0])
                except KeyError:
                        parser.error('argument contains non-digits')
                else:
                        print("For {0}, say: {1}".format(args.num[0], result))
def main2():
        num_str = input("please input a number: ")
        print("{0} = {1}".format(num_str, num2words(num_str)))
if __name__ == "__main__":
        main()
else:
        # print("__name__: ", __name__)
        print("n2w loaded as a model")