# ItemResponseSetMembershipsAttributesInnerResponseAttributes

Response to be included in the Response Set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Response | 
**corresponding_status** | **str** | Item Status that the Response corresponds to | 

## Example

```python
from procore_sdk.models.item_response_set_memberships_attributes_inner_response_attributes import ItemResponseSetMembershipsAttributesInnerResponseAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponseSetMembershipsAttributesInnerResponseAttributes from a JSON string
item_response_set_memberships_attributes_inner_response_attributes_instance = ItemResponseSetMembershipsAttributesInnerResponseAttributes.from_json(json)
# print the JSON string representation of the object
print(ItemResponseSetMembershipsAttributesInnerResponseAttributes.to_json())

# convert the object into a dict
item_response_set_memberships_attributes_inner_response_attributes_dict = item_response_set_memberships_attributes_inner_response_attributes_instance.to_dict()
# create an instance of ItemResponseSetMembershipsAttributesInnerResponseAttributes from a dict
item_response_set_memberships_attributes_inner_response_attributes_from_dict = ItemResponseSetMembershipsAttributesInnerResponseAttributes.from_dict(item_response_set_memberships_attributes_inner_response_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


