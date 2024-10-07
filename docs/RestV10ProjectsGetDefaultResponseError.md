# RestV10ProjectsGetDefaultResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Top level HTTP status code | 
**message** | **str** | Error message description | 
**details** | [**List[RestV10ProjectsGetDefaultResponseErrorDetailsInner]**](RestV10ProjectsGetDefaultResponseErrorDetailsInner.md) | Additional information to convey how to fix the error | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_get_default_response_error import RestV10ProjectsGetDefaultResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsGetDefaultResponseError from a JSON string
rest_v10_projects_get_default_response_error_instance = RestV10ProjectsGetDefaultResponseError.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsGetDefaultResponseError.to_json())

# convert the object into a dict
rest_v10_projects_get_default_response_error_dict = rest_v10_projects_get_default_response_error_instance.to_dict()
# create an instance of RestV10ProjectsGetDefaultResponseError from a dict
rest_v10_projects_get_default_response_error_from_dict = RestV10ProjectsGetDefaultResponseError.from_dict(rest_v10_projects_get_default_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


