import xml.etree.ElementTree as ET

data = '''
    <stuff>
        <users>
            <user x='2'>
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x='7'>
                <id>002</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>
'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('There are ' + str(len(lst)) +  ' users.\n')
for item in lst:
    print('Name - ', item.findtext('name'))
    print('ID - ', item.findtext('id'))
    print('Attr - ', item.get('x'), '\n')