from aocd import data
import re


def process(data, is_valid):
    pp = data.split('\n\n')
    pp_fields = [{ k:v for k,v in (f.split(':') for f in p.split()) } for p in pp]

    valid = 0
    for p in pp_fields:
        valid += int(is_valid(p))

    return str(valid)

def part_a(data):
    def is_valid(p):
        ALL_KEYS = set({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'})
        NPC_KEYS = ALL_KEYS - set({'cid'})
        return (p.keys() == ALL_KEYS) or (p.keys() == NPC_KEYS)
        
    return process(data, is_valid)

def part_b(data):
    def height_valid(hgt):
        valid = False
        m = re.match(r'(\d+)(cm|in)', hgt)
        if m:
            if m.group(2) == 'cm':
                valid = 150 <= int(m.group(1)) <= 193
            if m.group(2) == 'in':
                valid = 59 <= int(m.group(1)) <= 76
        return valid

    def is_valid(p):
        ALL_KEYS = set({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'})
        NPC_KEYS = ALL_KEYS - set({'cid'})

        return bool(
            ((p.keys() == ALL_KEYS) or (p.keys() == NPC_KEYS)) and
            ( 1920 <= int(p['byr']) <= 2002 ) and
            ( 2010 <= int(p['iyr']) <= 2020 ) and
            ( 2020 <= int(p['eyr']) <= 2030 ) and
            ( height_valid(p['hgt']) ) and
            ( re.match(r'^#[0-9a-f]{6}$', p['hcl'])) and
            ( re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', p['ecl'])) and
            ( re.match(r'^\d{9}$', p['pid']) )
        )

    return process(data, is_valid)

test_data = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_data_b = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

if __name__ == "__main__":
    assert part_a(test_data) == "2"
    assert part_b(test_data_b) == "4"
    print(part_a(data))
    print(part_b(data))
