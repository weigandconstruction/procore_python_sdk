# OauthTokenInfoGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_owner_id** | **int** | Resource owner ID | [optional] 
**scopes** | **List[str]** | Scopes | [optional] 
**expires_in_seconds** | **int** | Expiration time in seconds | [optional] 
**application** | [**OauthTokenInfoGet200ResponseApplication**](OauthTokenInfoGet200ResponseApplication.md) |  | [optional] 
**created_at** | **int** | The integer value representing the time the access token was created. | [optional] 

## Example

```python
from procore_sdk.models.oauth_token_info_get200_response import OauthTokenInfoGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OauthTokenInfoGet200Response from a JSON string
oauth_token_info_get200_response_instance = OauthTokenInfoGet200Response.from_json(json)
# print the JSON string representation of the object
print(OauthTokenInfoGet200Response.to_json())

# convert the object into a dict
oauth_token_info_get200_response_dict = oauth_token_info_get200_response_instance.to_dict()
# create an instance of OauthTokenInfoGet200Response from a dict
oauth_token_info_get200_response_from_dict = OauthTokenInfoGet200Response.from_dict(oauth_token_info_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


