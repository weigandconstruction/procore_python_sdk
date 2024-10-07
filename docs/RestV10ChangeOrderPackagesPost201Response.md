# RestV10ChangeOrderPackagesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due date | [optional] 
**executed** | **bool** | Executed | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**position** | **int** | Position | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**review_notes** | **str** | Notes to assist the reviewer | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**revised_substantial_completion_date** | **date** | Revised substantial completion date | [optional] 
**revision** | **int** | Revision number | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**signed_change_order_received_date** | **date** | Signed change order received date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**type** | **str** | Type | [optional] 
**updated_at** | **datetime** |  | [optional] 
**creator** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**designated_reviewer** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**reviewer** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 
**line_items** | [**List[RestV10ChangeOrderPackagesPost201ResponseLineItemsInner]**](RestV10ChangeOrderPackagesPost201ResponseLineItemsInner.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_post201_response import RestV10ChangeOrderPackagesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesPost201Response from a JSON string
rest_v10_change_order_packages_post201_response_instance = RestV10ChangeOrderPackagesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesPost201Response.to_json())

# convert the object into a dict
rest_v10_change_order_packages_post201_response_dict = rest_v10_change_order_packages_post201_response_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesPost201Response from a dict
rest_v10_change_order_packages_post201_response_from_dict = RestV10ChangeOrderPackagesPost201Response.from_dict(rest_v10_change_order_packages_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


