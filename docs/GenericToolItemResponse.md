# GenericToolItemResponse

Generic Tool Item Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Drawing Upload ID | [optional] 
**notes** | **str** | The text of the Response | [optional] 
**created_at** | **datetime** | Generic Tool Item Response created at | [optional] 
**official** | **bool** | If the response is an Official Response | [optional] 
**position** | **int** | Position of the Response | [optional] 
**status** | **str** | Status of the Generic Tool Item Response | [optional] 
**created_by** | [**RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner**](RestV10ProjectsProjectIdRfisDefaultDistributionGet200ResponseInner.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item_response import GenericToolItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItemResponse from a JSON string
generic_tool_item_response_instance = GenericToolItemResponse.from_json(json)
# print the JSON string representation of the object
print(GenericToolItemResponse.to_json())

# convert the object into a dict
generic_tool_item_response_dict = generic_tool_item_response_instance.to_dict()
# create an instance of GenericToolItemResponse from a dict
generic_tool_item_response_from_dict = GenericToolItemResponse.from_dict(generic_tool_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


