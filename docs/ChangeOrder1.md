# ChangeOrder1

Change Order object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_ids** | **List[int]** | Existing attachments to preserve on the response | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 
**contract_id** | **int** | Unique identifier for the contract. | 
**batch_id** | **int** | Unique identifier for a change order batch. | [optional] 
**change_order_change_reason_id** | **int** | Unique identifier for the change reason. | [optional] 
**location_id** | **int** | Unique identifier for the location. | [optional] 
**designated_reviewer_id** | **int** | Unique identifier for the designated reviewer. This field is only supported for single-tier projects. Behavior is undefined in multi-tier projects. | [optional] 
**received_from_id** | **int** | Unique identifier for the received from entity. | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due Date | [optional] 
**paid_date** | **date** | Paid Date | [optional] 
**invoiced_date** | **date** | Invoiced Date | [optional] 
**title** | **str** | Title of the Contract | [optional] 
**status** | **str** | Status | [optional] 
**reference** | **str** | Reference | [optional] 
**number** | **str** | Number of the Change Order | [optional] 
**revision** | **int** | Revision Number | [optional] 
**field_change** | **bool** | Field Change | [optional] 
**signature_required** | **bool** | Whether a signature will be required for this Change Order | [optional] 
**signed_change_order_received_date** | **date** | Signed Change Order Received Date | [optional] 
**schedule_impact_amount** | **int** | Schedule impact in days | [optional] 
**executed** | **bool** | Whether or not the Change Order is executed | [optional] 
**private** | **bool** | Whether or not the Commitment Change Order is private | [optional] 
**paid** | **bool** | Whether or not the Commitment Change Order is paid | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.change_order1 import ChangeOrder1

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOrder1 from a JSON string
change_order1_instance = ChangeOrder1.from_json(json)
# print the JSON string representation of the object
print(ChangeOrder1.to_json())

# convert the object into a dict
change_order1_dict = change_order1_instance.to_dict()
# create an instance of ChangeOrder1 from a dict
change_order1_from_dict = ChangeOrder1.from_dict(change_order1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


