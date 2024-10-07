# GenericToolItem1

Generic Tool Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the Generic Tool Item | [optional] 
**closed_at** | **datetime** | Generic Tool Item closed at | [optional] 
**created_at** | **datetime** | Generic Tool Item created at | [optional] 
**description** | **str** | Description of a Generic Tool Item | [optional] 
**due_date** | **date** | Generic Tool Item Due Date | [optional] 
**issued_at** | **datetime** | Generic Tool Item issued at | [optional] 
**origin_generic_tool_item_id** | **int** | Origin Generic Tool Item ID | [optional] 
**origin_rfi_id** | **int** | Origin RFI ID | [optional] 
**position** | **str** | The Number of the Generic Tool Item | [optional] 
**private** | **bool** | If the Generic Tool Item is private | [optional] 
**schedule_impact** | [**GenericToolItem1ScheduleImpact**](GenericToolItem1ScheduleImpact.md) |  | [optional] 
**cost_impact** | [**GenericToolItem1CostImpact**](GenericToolItem1CostImpact.md) |  | [optional] 
**updated_at** | **datetime** | Generic Tool Item updated at | [optional] 
**status** | **str** | Status of the Generic Tool Item | [optional] 
**status_type** | **str** | The default status the Generic Tool Item&#39;s status is mapped to. | [optional] 
**title** | **str** | Title of the Generic Tool Item | [optional] 
**created_by** | [**GenericToolItem1CreatedBy**](GenericToolItem1CreatedBy.md) |  | [optional] 
**received_from** | [**GenericToolItem1CreatedBy**](GenericToolItem1CreatedBy.md) |  | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**cost_code** | [**Compact**](Compact.md) |  | [optional] 
**specification_section** | [**RestV10SpecificationSectionsGet200ResponseInner**](RestV10SpecificationSectionsGet200ResponseInner.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**trades** | [**List[Trade]**](Trade.md) | Trades | [optional] 
**tasks** | [**List[GenericToolItemTasksInner]**](GenericToolItemTasksInner.md) | Tasks | [optional] 
**sub_job** | [**SubJob1**](SubJob1.md) |  | [optional] 
**generic_tool** | [**RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response**](RestV10CompaniesCompanyIdGenericToolsGenericToolIdPatch200Response.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Attachments | [optional] 
**document_management_document_revision_ids** | **List[str]** | PDM document revision IDs | [optional] 
**distribution_members** | [**List[GenericToolItem1CreatedBy]**](GenericToolItem1CreatedBy.md) | Distribution Members | [optional] 
**assignees** | [**List[GenericToolItem1CreatedBy]**](GenericToolItem1CreatedBy.md) | Assignees | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.generic_tool_item1 import GenericToolItem1

# TODO update the JSON string below
json = "{}"
# create an instance of GenericToolItem1 from a JSON string
generic_tool_item1_instance = GenericToolItem1.from_json(json)
# print the JSON string representation of the object
print(GenericToolItem1.to_json())

# convert the object into a dict
generic_tool_item1_dict = generic_tool_item1_instance.to_dict()
# create an instance of GenericToolItem1 from a dict
generic_tool_item1_from_dict = GenericToolItem1.from_dict(generic_tool_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


