import json, requests
key = 'KEY'

MONTHS = ["", "OCAK", "ŞUBAT", "MART", "NİSAN", "MAYIS", "HAZİRAN", "TEMMUZ", "AĞUSTOS", "EYLÜL", "EKİM", "KASIM", "ARALIK"]
def toTag(s):
    return MONTHS[int(s[5:7])] + ' ' + s[0:4]

pageToken = None
while True:
    append = ''
    if pageToken:
        append = '&pageToken=' + pageToken
    request = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&key='
                           + key + '&playlistId=UUhqfxzORYlvMezSVmQfo3IQ' + append)
    response = json.loads(request.content)

    for item in response['items']:
        v = item['snippet']
        print('- image: ' + v['resourceId']['videoId'])
        print('  tag: ' + toTag(v['publishedAt']))
        print('  title: \"' + v['title'] + '\"')
        print()

    if 'nextPageToken' in response:
        pageToken = response['nextPageToken']
    else:
        break

