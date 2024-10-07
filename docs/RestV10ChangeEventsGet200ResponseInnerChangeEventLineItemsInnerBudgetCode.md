# RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode

Item's associated Budget Code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**flat_code** | **str** | wbs code flat code | [optional] 
**description** | **str** | wbs code description | [optional] 
**segment_items** | [**List[RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner]**](RestV10CompaniesCompanyIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsGet200ResponseInner.md) | Work breakdown structure segment items | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode from a JSON string
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code_instance = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode.to_json())

# convert the object into a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code_dict = rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code_instance.to_dict()
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode from a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code_from_dict = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode.from_dict(rest_v10_change_events_get200_response_inner_change_event_line_items_inner_budget_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


