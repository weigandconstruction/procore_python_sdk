# BidAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**item_type** | **str** | Type of item attachment belongs to | [optional] 
**prostore_file_id** | **int** | prostore file ID | [optional] 
**url** | **str** | URL | [optional] 
**name** | **str** | Filename | [optional] 

## Example

```python
from procore_sdk.models.bid_attachments_inner import BidAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BidAttachmentsInner from a JSON string
bid_attachments_inner_instance = BidAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(BidAttachmentsInner.to_json())

# convert the object into a dict
bid_attachments_inner_dict = bid_attachments_inner_instance.to_dict()
# create an instance of BidAttachmentsInner from a dict
bid_attachments_inner_from_dict = BidAttachmentsInner.from_dict(bid_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


