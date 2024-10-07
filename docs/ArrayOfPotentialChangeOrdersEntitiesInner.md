# ArrayOfPotentialChangeOrdersEntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**change_order_change_reason_id** | **int** | Change Reason ID | [optional] 
**change_order_request_id** | **int** | Change Order Request ID | [optional] 
**commitment_change_event_id** | **int** | Commitment Change Event ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**creator** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**designated_reviewer** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**due_date** | **datetime** | Due date | [optional] 
**field_change** | **bool** | Field change | [optional] 
**grand_total** | **float** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**line_items** | [**List[ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner]**](ArrayOfPotentialChangeOrdersEntitiesInnerLineItemsInner.md) |  | [optional] 
**line_items_extended_total** | **float** | Line items extended total | [optional] 
**line_items_total** | **float** | Line items total | [optional] 
**location_id** | **int** | Location ID | [optional] 
**number** | **str** | Number | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid** | **bool** | Paid | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**position** | **int** | Position | [optional] 
**prime_change_event_id** | **int** | Prime Contract Change Event ID | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**reason** | **str** | Reason | [optional] 
**received_from** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**reference** | **str** | Reference | [optional] 
**request_for_quote_id** | **int** | RFQ ID | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**reviewer** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**revision** | **int** | Revision | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**vendor** | [**RestV10PrimeContractsGet200ResponseInnerContractor**](RestV10PrimeContractsGet200ResponseInnerContractor.md) |  | [optional] 
**void** | **bool** | Void | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_potential_change_orders_entities_inner import ArrayOfPotentialChangeOrdersEntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInner from a JSON string
array_of_potential_change_orders_entities_inner_instance = ArrayOfPotentialChangeOrdersEntitiesInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfPotentialChangeOrdersEntitiesInner.to_json())

# convert the object into a dict
array_of_potential_change_orders_entities_inner_dict = array_of_potential_change_orders_entities_inner_instance.to_dict()
# create an instance of ArrayOfPotentialChangeOrdersEntitiesInner from a dict
array_of_potential_change_orders_entities_inner_from_dict = ArrayOfPotentialChangeOrdersEntitiesInner.from_dict(array_of_potential_change_orders_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


