# A tool to parse the "Sheep and goat health log" into CSV files
# for database import

import argparse
from argparse import RawTextHelpFormatter


class FormatHealth():
    def __init__(self, animal_file, animal_tag_id):
        self.animal_file = animal_file
        self.animal_tag_id = animal_tag_id

    def format_health(self):
        with open(self.animal_file) as f:
            content = f.readlines()
        output = []
        first = True
        for line in content:
            # First line has some weird character, skip it
            if first:
                first = False
                continue

            line = line.strip()

            line = line.replace('copper bolus (g)', '1')
            line = line.replace('Dewormer', '2')
            line = line.replace('drench (ml)', '3')
            line = line.replace('Drench (ml)', '3')
            line = line.replace('famacha', '4')
            line = line.replace('Famacha', '4')
            line = line.replace('hoof', '5')
            line = line.replace('Hoof', '5')
            line = line.replace('mayo Colbolt w/CU', '6')
            line = line.replace('Mayo Colbolt w/CU', '6')
            line = line.replace('mayo Colbolt wo/CU', '7')
            line = line.replace('Mayo Colbolt wo/CU', '7')
            line = line.replace('shear', '10')
            line = line.replace('Shear', '10')
            line = line.replace('selenium (ml)', '9')

            line = line.replace('2019-0601', '2019-06-01')

            if line.startswith(',') or line.endswith(','):
                continue

            if 'fecal' in line:
                continue

            line = ',' + self.animal_tag_id + ',' + line

            output.append(line)
        with open(self.animal_file + '.edit.csv', 'w') as f:
            for out in output:
                f.write("%s\n" % out)


def main():
    parser = argparse.ArgumentParser(
        description="Animal health reformatter", add_help=True, formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--animal_file', required=True, help='File with exported animal data')
    parser.add_argument('-a', '--animal_tag_id', required=True, help='Ear tag ID for animal')
    args = parser.parse_args()

    print('\nRecevied arguments as:')
    print('    animal_file:     {}'.format(args.animal_file))
    print('    animal_tag_id:   {}'.format(args.animal_tag_id))

    print('\nFormating health file...')
    fh = FormatHealth(args.animal_file, args.animal_tag_id)
    fh.format_health()
    print('Complete\n')


if __name__ == '__main__':
    main()
