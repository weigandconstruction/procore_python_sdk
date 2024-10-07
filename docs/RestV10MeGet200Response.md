# RestV10MeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**login** | **str** | The email address that the user uses to log into Procore. | [optional] 
**name** | **str** | User name. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_me_get200_response import RestV10MeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10MeGet200Response from a JSON string
rest_v10_me_get200_response_instance = RestV10MeGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10MeGet200Response.to_json())

# convert the object into a dict
rest_v10_me_get200_response_dict = rest_v10_me_get200_response_instance.to_dict()
# create an instance of RestV10MeGet200Response from a dict
rest_v10_me_get200_response_from_dict = RestV10MeGet200Response.from_dict(rest_v10_me_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


