# WbsCodeBulkCreateBulkInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the wbs code. | [optional] 
**segment_items** | [**List[WbsCodeBulkCreateBulkInnerSegmentItemsInner]**](WbsCodeBulkCreateBulkInnerSegmentItemsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.wbs_code_bulk_create_bulk_inner import WbsCodeBulkCreateBulkInner

# TODO update the JSON string below
json = "{}"
# create an instance of WbsCodeBulkCreateBulkInner from a JSON string
wbs_code_bulk_create_bulk_inner_instance = WbsCodeBulkCreateBulkInner.from_json(json)
# print the JSON string representation of the object
print(WbsCodeBulkCreateBulkInner.to_json())

# convert the object into a dict
wbs_code_bulk_create_bulk_inner_dict = wbs_code_bulk_create_bulk_inner_instance.to_dict()
# create an instance of WbsCodeBulkCreateBulkInner from a dict
wbs_code_bulk_create_bulk_inner_from_dict = WbsCodeBulkCreateBulkInner.from_dict(wbs_code_bulk_create_bulk_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


