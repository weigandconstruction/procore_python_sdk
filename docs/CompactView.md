# CompactView

Project User Compact View

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | User first name | [optional] 
**id** | **int** | User id | [optional] 
**initials** | **str** | User initials | [optional] 
**last_name** | **str** | User last name | [optional] 
**name** | **str** | User full name | [optional] 
**vendor** | [**RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor**](RestV10ProjectsProjectIdPunchItemAssignmentsIdGet200ResponseVendor.md) |  | [optional] 

## Example

```python
from procore_sdk.models.compact_view import CompactView

# TODO update the JSON string below
json = "{}"
# create an instance of CompactView from a JSON string
compact_view_instance = CompactView.from_json(json)
# print the JSON string representation of the object
print(CompactView.to_json())

# convert the object into a dict
compact_view_dict = compact_view_instance.to_dict()
# create an instance of CompactView from a dict
compact_view_from_dict = CompactView.from_dict(compact_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


