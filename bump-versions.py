import os
import re
from os.path import join

base_dir = 'castle/theme/theme_resources'

html_files = [
    join(base_dir, 'index.html'),
    join(base_dir, 'frontpage.html'),
    join(base_dir, 'page.html'),
]


def bump_versions(html):
    for group in re.findall('(?P<version>[\/\.\w\?]+v=[0-9]+)', html):
        url, version = group.split('?')
        version = int(version.replace('v=', '')) + 1
        html = html.replace(group, '{}?v={}'.format(url, version))
    return html


if __name__ == '__main__':
    for filename in html_files:
        fi = open(filename)
        html = fi.read()
        fi.close()
        new_html = bump_versions(html)
        fi = open(filename, 'w')
        fi.write(new_html)
        fi.close()
