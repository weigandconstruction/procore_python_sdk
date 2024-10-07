# RestV10RequisitionsGet200ResponseInner

Requisition (Subcontractor Invoice)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID (present in all views) | [optional] 
**project_id** | **int** | Project ID (present in all views) | [optional] 
**electronic_signature_id** | **int** | Eletronic Signature ID (present in all views) | [optional] 
**billing_date** | **date** | Billing date (present in all views) | [optional] 
**commitment_id** | **int** | commitment ID (present in all views) | [optional] 
**commitment_type** | **str** | Commitment Type (present in all views) | [optional] 
**contract_name** | **str** | Contract Name (present in all views) | [optional] 
**created_at** | **datetime** | Date req was created (present in all views) | [optional] 
**created_by** | [**RestV11RequisitionsGet200ResponseInnerCreatedBy**](RestV11RequisitionsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**updated_at** | **datetime** | Date req was last updated (present in all views) | [optional] 
**invoice_number** | **str** | Invoice number (present in all views) | [optional] 
**origin_data** | **str** | Requisition (Subcontractor Invoice) third party data (present in all views) | [optional] 
**origin_id** | **str** | Requisition (Subcontractor Invoice) third party ID (present in all views) | [optional] 
**payment_date** | **date** | Date requisition was paid (present in all views) | [optional] 
**period_id** | **int** | Period ID (present in all views) | [optional] 
**requisition_start** | **date** | Requisition (Subcontractor Invoice) start date (present in all views) | [optional] 
**requisition_end** | **date** | Requisition (Subcontractor Invoice) end date (present in all views) | [optional] 
**status** | **str** | Status (present in all views) | [optional] 
**erp_status** | **str** |  | [optional] 
**submitted_at** | **date** | Date requisition was submitted (present in all views) | [optional] 
**comment** | **str** | Comment (present in all views) | [optional] 
**final** | **bool** | true or false value indicating whether or not this is the final invoice (present in all views) | [optional] 
**number** | **int** | Requisition (Subcontractor Invoice) number (present in all views) | [optional] 
**percent_complete** | **str** | Percent complete (present in all views) | [optional] 
**vendor_name** | **str** | Name of Vendor for Invoice (present in all views) | [optional] 
**total_claimed_amount** | **str** | Total Claimed Amount for the Invoice (present in all views) | [optional] 
**deletable** | **bool** | A boolean indicating whether or not the invoice can be deleted. (present in all views) | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**currency_configuration** | [**RestV10RequisitionsGet200ResponseInnerCurrencyConfiguration**](RestV10RequisitionsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**attachments** | [**List[RestV11RequisitionsGet200ResponseInnerAttachmentsInner]**](RestV11RequisitionsGet200ResponseInnerAttachmentsInner.md) | Attachments (present in all views) | [optional] 
**summary** | [**RestV10RequisitionsGet200ResponseInnerSummary**](RestV10RequisitionsGet200ResponseInnerSummary.md) |  | [optional] 
**action_policy** | **object** | Object that describes the action policy for the item (present in action_policy or extended views) | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_requisitions_get200_response_inner import RestV10RequisitionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RequisitionsGet200ResponseInner from a JSON string
rest_v10_requisitions_get200_response_inner_instance = RestV10RequisitionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10RequisitionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_requisitions_get200_response_inner_dict = rest_v10_requisitions_get200_response_inner_instance.to_dict()
# create an instance of RestV10RequisitionsGet200ResponseInner from a dict
rest_v10_requisitions_get200_response_inner_from_dict = RestV10RequisitionsGet200ResponseInner.from_dict(rest_v10_requisitions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


