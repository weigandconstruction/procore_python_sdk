# RestV10ProjectsGetDefaultResponseErrorDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | One of the standard error codes. The code should describe the error type and not the source. Computer consumable. | 
**message** | **str** | Localized message describing the error in human consumable language. | 
**source** | **str** | Field or source of error. Computer consumable. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_get_default_response_error_details_inner import RestV10ProjectsGetDefaultResponseErrorDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsGetDefaultResponseErrorDetailsInner from a JSON string
rest_v10_projects_get_default_response_error_details_inner_instance = RestV10ProjectsGetDefaultResponseErrorDetailsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsGetDefaultResponseErrorDetailsInner.to_json())

# convert the object into a dict
rest_v10_projects_get_default_response_error_details_inner_dict = rest_v10_projects_get_default_response_error_details_inner_instance.to_dict()
# create an instance of RestV10ProjectsGetDefaultResponseErrorDetailsInner from a dict
rest_v10_projects_get_default_response_error_details_inner_from_dict = RestV10ProjectsGetDefaultResponseErrorDetailsInner.from_dict(rest_v10_projects_get_default_response_error_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


