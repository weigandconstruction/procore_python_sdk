# ItemResponseSet

Item Response Set object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Response Set | 
**active** | **bool** | Indicates whether a Response Set is available for use | [optional] 
**memberships_attributes** | [**List[ItemResponseSetMembershipsAttributesInner]**](ItemResponseSetMembershipsAttributesInner.md) | Array of Response Set Memberships (Responses) | [optional] 

## Example

```python
from procore_sdk.models.item_response_set import ItemResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponseSet from a JSON string
item_response_set_instance = ItemResponseSet.from_json(json)
# print the JSON string representation of the object
print(ItemResponseSet.to_json())

# convert the object into a dict
item_response_set_dict = item_response_set_instance.to_dict()
# create an instance of ItemResponseSet from a dict
item_response_set_from_dict = ItemResponseSet.from_dict(item_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


