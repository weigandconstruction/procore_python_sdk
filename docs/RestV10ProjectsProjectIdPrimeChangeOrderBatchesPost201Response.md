# RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response

Prime Change Order Batch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Default2AttachmentsInner]**](Default2AttachmentsInner.md) | Attachments | [optional] 
**id** | **int** | Prime Change Order Batch ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**description** | **str** | Description of the Prime Change Order Batch | [optional] 
**due_date** | **date** | Due date | [optional] 
**executed** | **bool** | Whether or not the Prime Change Order Batch is executed | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**number** | **str** | Number | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**private** | **bool** | Only show this Contract to Admins and specific Accessors | [optional] 
**review_notes** | **str** | Notes to assist the reviewer | [optional] 
**reviewed_at** | **datetime** | Reviewed at | [optional] 
**revised_substantial_completion_date** | **date** | Revised substantial completion date | [optional] 
**revision** | **int** | Revision number | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**signature_required** | **bool** | Whether or not a signature is required on the Prime Change Order | [optional] 
**signed_change_order_received_date** | **date** | Signed change order received date | [optional] 
**status** | **str** | The status of the Prime Change Order | [optional] 
**title** | **str** | Title | [optional] 
**type** | **str** | Type | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200ResponseCreatedBy**](RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200ResponseCreatedBy.md) |  | [optional] 
**designated_reviewer** | [**RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200ResponseDesignatedReviewer**](RestV10ProjectsProjectIdPrimeChangeOrderBatchesGet200ResponseDesignatedReviewer.md) |  | [optional] 
**reviewed_by** | [**Default1ReviewedBy**](Default1ReviewedBy.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_prime_change_order_batches_post201_response import RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response from a JSON string
rest_v10_projects_project_id_prime_change_order_batches_post201_response_instance = RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_prime_change_order_batches_post201_response_dict = rest_v10_projects_project_id_prime_change_order_batches_post201_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response from a dict
rest_v10_projects_project_id_prime_change_order_batches_post201_response_from_dict = RestV10ProjectsProjectIdPrimeChangeOrderBatchesPost201Response.from_dict(rest_v10_projects_project_id_prime_change_order_batches_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


