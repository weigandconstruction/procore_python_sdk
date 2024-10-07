# RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**code** | **str** | Code | [optional] 
**name** | **str** | Name | [optional] 
**path_ids** | **List[int]** | Path variable IDs | [optional] 
**path_codes** | **List[str]** | Path variable codes | [optional] 
**segment_type** | **str** | Segment Type | [optional] 
**segment_id** | **int** | Segment ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_segment_items_inner import RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner from a JSON string
rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_segment_items_inner_instance = RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_segment_items_inner_dict = rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_segment_items_inner_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner from a dict
rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_segment_items_inner_from_dict = RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner.from_dict(rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_segment_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


