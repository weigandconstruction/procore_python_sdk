# Item

Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Item | [optional] 
**position** | **int** | The Position of the Item | [optional] 
**status** | **str** | The Status of the item | [optional] 
**response_id** | **int** | ID of the response if using multiple response sets, otherwise null | [optional] 
**item_attachments_attributes** | [**List[ItemItemAttachmentsAttributesInner]**](ItemItemAttachmentsAttributesInner.md) | An array of the Item&#39;s Attachments attributes | [optional] 

## Example

```python
from procore_sdk.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


