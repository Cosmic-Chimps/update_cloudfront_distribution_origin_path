import subprocess
import sys
import json
import os

distributionId = sys.argv[1]
s3OriginPath = sys.argv[2]
cfOriginIndex = sys.argv[3]

print('Get distribution \n')
proc = subprocess.Popen(['aws', 'cloudfront', 'get-distribution', '--id', distributionId] , stdout=subprocess.PIPE)
output = proc.stdout.read()

distConfig = json.loads(output)

originItem = distConfig['Distribution']['DistributionConfig']['Origins']['Items'][cfOriginIndex]
eTag = distConfig['ETag']

originItem['OriginPath'] = s3OriginPath

distConfigJson = json.dumps(distConfig['Distribution']['DistributionConfig'])

os.mkdir('.tmp')
f = open('.tmp/newdist.json', 'w')
f.write(distConfigJson)
f.close()

updateCommand = ['aws', 'cloudfront', 'update-distribution', '--id', distributionId , '--if-match', eTag, '--distribution-config', 'file://.tmp/newdist.json']

print('Update distribution')
proc = subprocess.Popen(updateCommand , stdout=subprocess.PIPE)
output = proc.stdout.read()

