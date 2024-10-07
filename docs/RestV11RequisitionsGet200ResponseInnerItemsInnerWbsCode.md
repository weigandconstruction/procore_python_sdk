# RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode

Item's associated Budget Code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**flat_code** | **str** | wbs code flat code | [optional] 
**description** | **str** | wbs code description | [optional] 
**segment_items** | [**List[RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner]**](RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCodeSegmentItemsInner.md) | Work breakdown structure segment items | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_items_inner_wbs_code import RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode from a JSON string
rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_instance = RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_dict = rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode from a dict
rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_from_dict = RestV11RequisitionsGet200ResponseInnerItemsInnerWbsCode.from_dict(rest_v11_requisitions_get200_response_inner_items_inner_wbs_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


