# RestV10ProjectsGetDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**RestV10ProjectsGetDefaultResponseError**](RestV10ProjectsGetDefaultResponseError.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_get_default_response import RestV10ProjectsGetDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsGetDefaultResponse from a JSON string
rest_v10_projects_get_default_response_instance = RestV10ProjectsGetDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsGetDefaultResponse.to_json())

# convert the object into a dict
rest_v10_projects_get_default_response_dict = rest_v10_projects_get_default_response_instance.to_dict()
# create an instance of RestV10ProjectsGetDefaultResponse from a dict
rest_v10_projects_get_default_response_from_dict = RestV10ProjectsGetDefaultResponse.from_dict(rest_v10_projects_get_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


