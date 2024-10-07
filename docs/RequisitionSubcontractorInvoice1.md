# RequisitionSubcontractorInvoice1

Requisition (Subcontractor Invoice)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RequisitionSubcontractorInvoice1ItemsInner]**](RequisitionSubcontractorInvoice1ItemsInner.md) |  | [optional] 
**period_id** | **int** | Period ID | [optional] 
**requisition_start** | **date** | Requisition (Subcontractor Invoice) start date | [optional] 
**requisition_end** | **date** | Requisition (Subcontractor Invoice) end date | [optional] 
**billing_date** | **date** | Billing date | [optional] 
**final** | **bool** | true or false value indicating whether or not this is the final invoice | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**payment_date** | **date** | Date requisition was paid | [optional] 
**origin_data** | **str** | Requisition (Subcontractor Invoice) third party data | [optional] 
**origin_id** | **str** | Requisition (Subcontractor Invoice) third party ID | [optional] 
**status** | **str** | Status; admin can set any status, standard and billing recipient can set to under_review (submit) or draft (save) | [optional] 
**submitted_at** | **date** | Date requisition was submitted | [optional] 
**prostore_file_ids** | **List[int]** | An array of Prostore File IDs. The Prostore Files will be associated with the Requisition (Subcontractor Invoice) as attachments. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.requisition_subcontractor_invoice1 import RequisitionSubcontractorInvoice1

# TODO update the JSON string below
json = "{}"
# create an instance of RequisitionSubcontractorInvoice1 from a JSON string
requisition_subcontractor_invoice1_instance = RequisitionSubcontractorInvoice1.from_json(json)
# print the JSON string representation of the object
print(RequisitionSubcontractorInvoice1.to_json())

# convert the object into a dict
requisition_subcontractor_invoice1_dict = requisition_subcontractor_invoice1_instance.to_dict()
# create an instance of RequisitionSubcontractorInvoice1 from a dict
requisition_subcontractor_invoice1_from_dict = RequisitionSubcontractorInvoice1.from_dict(requisition_subcontractor_invoice1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


