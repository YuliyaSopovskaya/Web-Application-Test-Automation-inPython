import yaml
from module import Site

with open ('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])
