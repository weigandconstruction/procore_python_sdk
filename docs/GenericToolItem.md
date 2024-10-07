# GenericToolItem

Generic Tool Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Generic Tool Item ID | [optional] 
**closed_at** | **datetime** | Generic Tool Item closed at | [optional] 
**created_at** | **datetime** | Generic Tool Item created at | [optional] 
**description** | **str** | Description of a Generic Tool Item | [optional] 
**due_date** | **date** | Generic Tool Item Due Date | [optional] 
**issued_at** | **datetime** | Generic Tool Item issued at | [optional] 
**origin_generic_tool_item_id** | **int** | Origin Generic Tool Item ID | [optional] 
**origin_rfi_id** | **int** | Origin RFI ID | [optional] 
**position** | **str** | The Number of the Generic Tool Item | [optional] 
**private** | **bool** | If the Generic Tool Item is private | [optional] 
**schedule_impact** | **str** | Amount of Schedule Impact | [optional] 
**updated_at** | **datetime** | Generic Tool Item updated at | [optional] 
**cost_impact** | **str** | Amount of Cost Impact | [optional] 
**status** | **str** | Status of the Generic Tool Item | [optional] 
**title** | **str** | Title of the Generic Tool Item | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**received_from** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**cost_code** | [**ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode**](ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInnerMarkupLineItemsInnerMarkupDestinationCostCode.md) |  | [optional] 
**specification_section** | [**RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection**](RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection.md) |  | [optional] 
**sub_job** | [**SubJob**](SubJob.md) |  | [optional] 
**tasks** | [**List[GenericToolItemTasksInner]**](GenericToolItemTasksInner.md) | Tasks | [optional] 
**trade** | [**Trade2**](Trade2.md) |  | [optional] 
**trades** | [**List[GenericToolItemTradesInner]**](GenericToolItemTradesInner.md) | Trades | [optional] 
**generic_tool** | [**GenericToolItemGenericTool**](GenericToolItemGenericTool.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Distribution Members | [optional] 
**assignees** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Assignees | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item import GenericToolItem

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItem from a JSON string
generic_tool_item_instance = GenericToolItem.from_json(json)
# print the JSON string representation of the object
print(GenericToolItem.to_json())

# convert the object into a dict
generic_tool_item_dict = generic_tool_item_instance.to_dict()
# create an instance of GenericToolItem from a dict
generic_tool_item_from_dict = GenericToolItem.from_dict(generic_tool_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


