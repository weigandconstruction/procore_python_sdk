# ChangeOrderBatch

Change Order Batch object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 
**contract_id** | **int** | Unique identifier for the contract. | 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due Date | [optional] 
**executed** | **bool** | Whether or not the Change Order Batch is executed | [optional] 
**invoiced_date** | **date** | Invoiced Date | [optional] 
**number** | **str** | Number of the Change Order Batch | [optional] 
**paid_date** | **date** | Paid Date | [optional] 
**private** | **bool** | Whether or not the Change Order Batch is private | [optional] 
**revised_substantial_completion_date** | **date** | Revised substantial completion date | [optional] 
**revision** | **int** | Revision Number | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**signature_required** | **bool** | Whether a signature will be required for this Change Order Batch | [optional] 
**signed_change_order_received_date** | **date** | Signed Change Order Batch Received Date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title of the Change Order Batch | [optional] 
**designated_reviewer_id** | **int** | Unique identifier for the designated reviewer. This field is only supported for single-tier projects. Behavior is undefined in multi-tier projects. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.change_order_batch import ChangeOrderBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOrderBatch from a JSON string
change_order_batch_instance = ChangeOrderBatch.from_json(json)
# print the JSON string representation of the object
print(ChangeOrderBatch.to_json())

# convert the object into a dict
change_order_batch_dict = change_order_batch_instance.to_dict()
# create an instance of ChangeOrderBatch from a dict
change_order_batch_from_dict = ChangeOrderBatch.from_dict(change_order_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


