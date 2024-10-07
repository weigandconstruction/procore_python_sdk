# WbsCodeBulkCreateBulkInnerSegmentItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_id** | **int** | Id of the Segment defined at the company level. | 
**segment_item_id** | **int** | Segment Item ID. If present, a Segment Item will not be implicitly created. | 

## Example

```python
from procore_sdk.models.wbs_code_bulk_create_bulk_inner_segment_items_inner import WbsCodeBulkCreateBulkInnerSegmentItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WbsCodeBulkCreateBulkInnerSegmentItemsInner from a JSON string
wbs_code_bulk_create_bulk_inner_segment_items_inner_instance = WbsCodeBulkCreateBulkInnerSegmentItemsInner.from_json(json)
# print the JSON string representation of the object
print(WbsCodeBulkCreateBulkInnerSegmentItemsInner.to_json())

# convert the object into a dict
wbs_code_bulk_create_bulk_inner_segment_items_inner_dict = wbs_code_bulk_create_bulk_inner_segment_items_inner_instance.to_dict()
# create an instance of WbsCodeBulkCreateBulkInnerSegmentItemsInner from a dict
wbs_code_bulk_create_bulk_inner_segment_items_inner_from_dict = WbsCodeBulkCreateBulkInnerSegmentItemsInner.from_dict(wbs_code_bulk_create_bulk_inner_segment_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


