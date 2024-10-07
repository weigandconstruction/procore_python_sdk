# RestV10ChangeTypesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**abbreviation** | **str** | Abbreviation | [optional] 
**company_id** | **int** | Company ID | [optional] 
**change_type** | **str** | Change Type | [optional] 
**show_in_select** | **bool** | Whether available for GUI selection | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_types_get200_response_inner import RestV10ChangeTypesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeTypesGet200ResponseInner from a JSON string
rest_v10_change_types_get200_response_inner_instance = RestV10ChangeTypesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeTypesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_change_types_get200_response_inner_dict = rest_v10_change_types_get200_response_inner_instance.to_dict()
# create an instance of RestV10ChangeTypesGet200ResponseInner from a dict
rest_v10_change_types_get200_response_inner_from_dict = RestV10ChangeTypesGet200ResponseInner.from_dict(rest_v10_change_types_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


