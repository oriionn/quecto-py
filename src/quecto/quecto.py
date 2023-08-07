import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class Quecto:
    def __init__(self, instanceUrl):
        if not instanceUrl.startswith('http'): instanceUrl = 'https://' + instanceUrl
        if not instanceUrl.endswith('/'): instanceUrl = instanceUrl + '/'
        self.instanceUrl = instanceUrl

    def shortUrl(self, link: str, password: str = "") -> dict:
        """
        Shorten a link
        :param link: The link to shorten
        :param password: The password to protect the link
        :rtype dict
        :return: The API response
        """

        body = {
            'link': link
        }
        if password != "":
            body['password'] = password

        mp_encoder = MultipartEncoder(
            fields=body
        )

        r = requests.post(self.instanceUrl + 'api/shorten', data=mp_encoder, headers={'Content-Type': mp_encoder.content_type})

        if r.status_code == 200:
            data = r.json()['data']
            data['error'] = False
            return data
        else:
            return {
                'status': r.status_code,
                'error': True,
            }

    def unshortUrl(self, link, password: str = "") -> dict:
        """
        Unshorten a link
        :param link: The shortened link to unshorten
        :param password: The password used to protect the shortened link
        :rtype dict
        :return: The API response
        """

        code = link.split('/')[-1]
        apiUrl = self.instanceUrl + 'api/s/' + code
        if password != "":
            apiUrl += '?password=' + password
        r = requests.get(apiUrl)
        if r.status_code == 200:
            data = r.json()['data']
            data['error'] = False
            return data
        else:
            return {
                'status': r.status_code,
                'error': True,
            }

    def isValidInstance(self) -> bool:
        """
        Verify if the instance is valid
        :rtype bool
        :return: If the instance is valid
        """

        r = requests.get(self.instanceUrl + 'api/quectoCheck')
        return r.status_code == 200
