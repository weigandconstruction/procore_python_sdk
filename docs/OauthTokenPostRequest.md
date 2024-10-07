# OauthTokenPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_type** | **str** | Use the value &#x60;authorization_code&#x60; when getting a new access token. Use &#x60;refresh_token&#x60; when refreshing an existing access token. Use &#x60;client_credentials&#x60; when using a Procore Service Account for authentication. | 
**client_id** | **str** | Client ID you were assigned when you registered your application. | 
**client_secret** | **str** | Client Secret you were assigned when you registered your application. | 
**code** | **str** | Value of the &#x60;authorization_code&#x60; retrieved from the &#x60;/oauth/authorize&#x60; call. Only required when getting a new access code. | [optional] 
**redirect_uri** | **str** | The URI that the user will be redirected to after they grant authorization to your application. For browser-based web applications, use a &#x60;https://&#x60; web address. For \&quot;headless\&quot; applications use &#x60;urn:ietf:wg:oauth:2.0:oob&#x60;. | [optional] 
**refresh_token** | **str** | The refresh token string. Only required when refreshing an access token. | [optional] 

## Example

```python
from procore_sdk.models.oauth_token_post_request import OauthTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthTokenPostRequest from a JSON string
oauth_token_post_request_instance = OauthTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print(OauthTokenPostRequest.to_json())

# convert the object into a dict
oauth_token_post_request_dict = oauth_token_post_request_instance.to_dict()
# create an instance of OauthTokenPostRequest from a dict
oauth_token_post_request_from_dict = OauthTokenPostRequest.from_dict(oauth_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


