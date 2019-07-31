import pickle
import re

# last_challange_dir = '../pc04_linkedlist/'
# with open(f'./nothings', 'w+') as new:
#     with open(f'{last_challange_dir}/nothings_0', 'r') as file:
#         new.write(file.read())
#     with open(f'{last_challange_dir}/nothings_1', 'r') as file:
#         new.write(file.read())

"""
Hypotheses:
1. all pickle bstrings start with b'\x80\x0<V>' where <V> is the version num
2. pickle bstrings (entire) end differently depending on the root object
3. for strings- they will end 'q\x00', directly after the last character
4. for arrays- they will end
"""

nothings = []

def test_pickle(objects, version):
    path = f'./pickle_test_v{version}'
    with open(path, 'w') as file:
        for obj in objects:
            obj_str = f'"{obj}"' if type(obj) is str else obj
            file.write(f'{obj_str}\t->\t')
            file.write(str(pickle.dumps(obj, protocol=version)))
            file.write('\n')

def get_nothings(path: str) -> [int]:
    text = ""
    with open(path, 'r') as file:
        text = file.read()
    return [int(nothing) for nothing in text.split('\n') if len(nothing) > 0]


def test_all():
    versions = range(0, 5)
    objects = [
        "{}",
        "a",
        "asflkjnqwrt",
        {'a': 'a'},
        {1: 1},
        [1, 2, 3],
        {'a': [1, 2, 3]},
        ['a', 'b']
    ]
    for version in versions:
        test_pickle(objects, version)


if __name__ == '__main__':
    test_all()
    exit(0)
    print()
    byts = None
    with open('peakhell.jpg', 'rb') as pic:
        byts = pic.read()
        # locations = [x.start() for x in ]
        print(re.findall(b'\x80\x04.{30}', byts))

    nothings = get_nothings('nothings')
    # print(min(nothings), max(nothings))