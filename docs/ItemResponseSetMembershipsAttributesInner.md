# ItemResponseSetMembershipsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_attributes** | [**ItemResponseSetMembershipsAttributesInnerResponseAttributes**](ItemResponseSetMembershipsAttributesInnerResponseAttributes.md) |  | [optional] 

## Example

```python
from procore_sdk.models.item_response_set_memberships_attributes_inner import ItemResponseSetMembershipsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemResponseSetMembershipsAttributesInner from a JSON string
item_response_set_memberships_attributes_inner_instance = ItemResponseSetMembershipsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(ItemResponseSetMembershipsAttributesInner.to_json())

# convert the object into a dict
item_response_set_memberships_attributes_inner_dict = item_response_set_memberships_attributes_inner_instance.to_dict()
# create an instance of ItemResponseSetMembershipsAttributesInner from a dict
item_response_set_memberships_attributes_inner_from_dict = ItemResponseSetMembershipsAttributesInner.from_dict(item_response_set_memberships_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


