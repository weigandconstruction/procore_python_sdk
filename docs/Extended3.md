# Extended3

Base Prime Change Order Extended View

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_events** | [**List[Extended3ChangeEventsInner]**](Extended3ChangeEventsInner.md) | Change Events linked | [optional] 
**id** | **int** | Prime Change Order ID | [optional] 
**batch_id** | **int** | Batch ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**legacy_package_id** | **int** | Legacy Package ID | [optional] 
**legacy_request_id** | **int** | Legacy Request ID | [optional] 
**location_id** | **int** | Location ID | [optional] 
**description** | **str** | Description of the Prime Change Order | [optional] 
**title** | **str** | Title | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**paid_date** | **date** | Paid date | [optional] 
**due_date** | **date** | Due date | [optional] 
**revised_substantial_completion_date** | **date** | Revised substantial completion date | [optional] 
**signed_change_order_received_date** | **date** | Signed change order received date | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**reviewed_at** | **datetime** | Approved date | [optional] 
**executed** | **bool** | Whether or not the Prime Change Order is executed | [optional] 
**paid** | **bool** | Whether or not the Prime Change Order is paid | [optional] 
**signature_required** | **bool** | Whether or not a signature is required on the Prime Change Order | [optional] 
**private** | **bool** | Only show this Contract to Admins and specific Accessors | [optional] 
**field_change** | **bool** | Field change | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**number** | **str** | Number | [optional] 
**type** | **str** | Type | [optional] 
**revision** | **int** | Revision number | [optional] 
**status** | **str** | The status of the Prime Change Order | [optional] 
**reference** | **str** | Reference | [optional] 
**created_by** | [**Default1CreatedBy**](Default1CreatedBy.md) |  | [optional] 
**designated_reviewer** | [**Default1DesignatedReviewer**](Default1DesignatedReviewer.md) |  | [optional] 
**received_from** | [**Default1ReceivedFrom**](Default1ReceivedFrom.md) |  | [optional] 
**reviewed_by** | [**Default1ReviewedBy**](Default1ReviewedBy.md) |  | [optional] 
**change_order_change_reason** | [**Default1ChangeOrderChangeReason**](Default1ChangeOrderChangeReason.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.extended3 import Extended3

# TODO update the JSON string below
json = "{}"
# create an instance of Extended3 from a JSON string
extended3_instance = Extended3.from_json(json)
# print the JSON string representation of the object
print(Extended3.to_json())

# convert the object into a dict
extended3_dict = extended3_instance.to_dict()
# create an instance of Extended3 from a dict
extended3_from_dict = Extended3.from_dict(extended3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


