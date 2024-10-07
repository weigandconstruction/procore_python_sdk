# RestV11RequisitionsGet200ResponseInner

Extended Requisition (Subcontractor Invoice)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**previous_requisition_id** | **int** | ID for the previous requisition before this one on the same contract | [optional] 
**project_id** | **int** | Project ID | [optional] 
**billing_date** | **date** | Billing date | [optional] 
**created_at** | **datetime** | Date req was created | [optional] 
**updated_at** | **datetime** | Date req was last updated | [optional] 
**commitment_id** | **int** | commitment ID | [optional] 
**commitment_type** | **str** | Commitment Type | [optional] 
**contract_name** | **str** | Contract Name | [optional] 
**deletable** | **bool** | A boolean indicating whether or not the invoice can be deleted. | [optional] 
**final** | **bool** | true or false value indicating whether or not this is the final invoice | [optional] 
**vendor_name** | **str** | Name of Vendor for Invoice | [optional] 
**vendor_id** | **int** | ID of Vendor for Invoice | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**invoice_type** | **str** | Invoice type (present in all views) | [optional] 
**origin_data** | **str** | Requisition (Subcontractor Invoice) third party data | [optional] 
**origin_id** | **str** | Requisition (Subcontractor Invoice) third party ID | [optional] 
**payment_date** | **date** | Date requisition was paid | [optional] 
**percent_complete** | **str** | Percent complete | [optional] 
**period_id** | **int** | Period ID | [optional] 
**requisition_start** | **date** | Requisition (Subcontractor Invoice) start date | [optional] 
**requisition_end** | **date** | Requisition (Subcontractor Invoice) end date | [optional] 
**status** | **str** | Status | [optional] 
**erp_status** | **str** | Current ERP status of Requisition | [optional] 
**number** | **int** | Requisition (Subcontractor Invoice) number | [optional] 
**submitted_at** | **date** | Date requisition was submitted | [optional] 
**total_claimed_amount** | **str** | Total Claimed Amount for the Invoice | [optional] 
**electronic_signature_id** | **int** | Electronic Signature ID | [optional] 
**move_materials_to_previous_work_completed** | **bool** | A boolean indicating if should move materials to previous work completed. | [optional] 
**summary_text** | [**RestV11RequisitionsGet200ResponseInnerSummaryText**](RestV11RequisitionsGet200ResponseInnerSummaryText.md) |  | [optional] 
**summary** | [**RestV11RequisitionsGet200ResponseInnerSummary**](RestV11RequisitionsGet200ResponseInnerSummary.md) |  | [optional] 
**created_by** | [**RestV11RequisitionsGet200ResponseInnerCreatedBy**](RestV11RequisitionsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 
**currency_configuration** | [**RestV11RequisitionsGet200ResponseInnerCurrencyConfiguration**](RestV11RequisitionsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**attachments** | [**List[RestV11RequisitionsGet200ResponseInnerAttachmentsInner]**](RestV11RequisitionsGet200ResponseInnerAttachmentsInner.md) | Attachments | [optional] 
**items** | [**List[RestV11RequisitionsGet200ResponseInnerItemsInner]**](RestV11RequisitionsGet200ResponseInnerItemsInner.md) | Requisition items. Included only when the views query param includes &#39;extended&#39; or &#39;items&#39;. | [optional] 
**item_packages** | [**List[RestV11RequisitionsGet200ResponseInnerItemPackagesInner]**](RestV11RequisitionsGet200ResponseInnerItemPackagesInner.md) | Requisition item packages. An item package can have either a contract or change order as its parent entity. Included only when the views query param includes &#39;extended&#39; or &#39;items&#39;. | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner import RestV11RequisitionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInner from a JSON string
rest_v11_requisitions_get200_response_inner_instance = RestV11RequisitionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_dict = rest_v11_requisitions_get200_response_inner_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInner from a dict
rest_v11_requisitions_get200_response_inner_from_dict = RestV11RequisitionsGet200ResponseInner.from_dict(rest_v11_requisitions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


