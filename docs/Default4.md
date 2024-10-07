# Default4

Commitment Change Order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[Default2AttachmentsInner]**](Default2AttachmentsInner.md) | Attachments | [optional] 
**id** | **int** | Commitment Change Order ID | [optional] 
**batch_id** | **int** | Batch ID | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**legacy_package_id** | **int** | Legacy Package ID | [optional] 
**legacy_request_id** | **int** | Legacy Request ID | [optional] 
**location_id** | **int** | Location ID | [optional] 
**description** | **str** | Description of the Commitment Change Order | [optional] 
**title** | **str** | Title | [optional] 
**invoiced_date** | **date** | Invoiced date | [optional] 
**due_date** | **date** | Due date | [optional] 
**revised_substantial_completion_date** | **date** | Revised substantial completion date | [optional] 
**signed_change_order_received_date** | **date** | Signed change order received date | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**reviewed_at** | **datetime** | Approved date | [optional] 
**executed** | **bool** | Whether or not the Commitment Change Order is executed | [optional] 
**paid** | **bool** | Whether or not the Commitment Change Order is paid | [optional] 
**signature_required** | **bool** | Whether or not a signature is required on the Commitment Change Order | [optional] 
**private** | **bool** | Only show this Contract to Admins and specific Accessors | [optional] 
**field_change** | **bool** | Field change | [optional] 
**grand_total** | **str** | Total including markup | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**number** | **str** | Number | [optional] 
**type** | **str** | Type | [optional] 
**revision** | **int** | Revision number | [optional] 
**status** | **str** | The status of the Commitment Change Order | [optional] 
**reference** | **str** | Reference | [optional] 
**created_by** | [**Default1CreatedBy**](Default1CreatedBy.md) |  | [optional] 
**designated_reviewer** | [**Default3DesignatedReviewer**](Default3DesignatedReviewer.md) |  | [optional] 
**received_from** | [**Default3ReceivedFrom**](Default3ReceivedFrom.md) |  | [optional] 
**reviewed_by** | [**Default3ReviewedBy**](Default3ReviewedBy.md) |  | [optional] 
**change_order_change_reason** | [**Default1ChangeOrderChangeReason**](Default1ChangeOrderChangeReason.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.default4 import Default4

# TODO update the JSON string below
json = "{}"
# create an instance of Default4 from a JSON string
default4_instance = Default4.from_json(json)
# print the JSON string representation of the object
print(Default4.to_json())

# convert the object into a dict
default4_dict = default4_instance.to_dict()
# create an instance of Default4 from a dict
default4_from_dict = Default4.from_dict(default4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


