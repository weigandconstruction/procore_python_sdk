# GenericToolItem1CreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**login** | **str** | Email | [optional] 
**name** | **str** | Name | [optional] 
**company** | [**GenericToolItem1CreatedByAllOfCompany**](GenericToolItem1CreatedByAllOfCompany.md) |  | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item1_created_by import GenericToolItem1CreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItem1CreatedBy from a JSON string
generic_tool_item1_created_by_instance = GenericToolItem1CreatedBy.from_json(json)
# print the JSON string representation of the object
print(GenericToolItem1CreatedBy.to_json())

# convert the object into a dict
generic_tool_item1_created_by_dict = generic_tool_item1_created_by_instance.to_dict()
# create an instance of GenericToolItem1CreatedBy from a dict
generic_tool_item1_created_by_from_dict = GenericToolItem1CreatedBy.from_dict(generic_tool_item1_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


