# OauthRevokePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Token | 
**client_id** | **str** | Client ID | 
**client_secret** | **str** | Client Secret | 

## Example

```python
from procore_sdk.models.oauth_revoke_post_request import OauthRevokePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthRevokePostRequest from a JSON string
oauth_revoke_post_request_instance = OauthRevokePostRequest.from_json(json)
# print the JSON string representation of the object
print(OauthRevokePostRequest.to_json())

# convert the object into a dict
oauth_revoke_post_request_dict = oauth_revoke_post_request_instance.to_dict()
# create an instance of OauthRevokePostRequest from a dict
oauth_revoke_post_request_from_dict = OauthRevokePostRequest.from_dict(oauth_revoke_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


