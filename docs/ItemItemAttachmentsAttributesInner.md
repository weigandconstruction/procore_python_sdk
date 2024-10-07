# ItemItemAttachmentsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prostore_file_id** | **int** | Attachment prostore file id | [optional] 
**created_by_id** | **int** | Attachment created by id | [optional] 
**item_id** | **int** | Attachment item id | [optional] 
**from_mobile** | **bool** | Attachment from mobile status | [optional] [default to False]

## Example

```python
from procore_sdk.models.item_item_attachments_attributes_inner import ItemItemAttachmentsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ItemItemAttachmentsAttributesInner from a JSON string
item_item_attachments_attributes_inner_instance = ItemItemAttachmentsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(ItemItemAttachmentsAttributesInner.to_json())

# convert the object into a dict
item_item_attachments_attributes_inner_dict = item_item_attachments_attributes_inner_instance.to_dict()
# create an instance of ItemItemAttachmentsAttributesInner from a dict
item_item_attachments_attributes_inner_from_dict = ItemItemAttachmentsAttributesInner.from_dict(item_item_attachments_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


