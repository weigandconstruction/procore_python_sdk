# RestV11RequisitionsGet200ResponseInnerSummaryText

Requisition (Subcontractor Invoice) summary text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | Name of the project | [optional] 
**project_number** | **str** | Number of the project | [optional] 
**to_general_contractor** | **str** | Name of the company the requisition is for | [optional] 
**requisition_period_start** | **date** | Requisition period start date | [optional] 
**requisition_period_end** | **date** | Requisition period end date | [optional] 
**subcontractor_name** | **str** | Name of the company the requisition is from | [optional] 
**subcontractor_street** | **str** | Street address of the company the requisition is from | [optional] 
**subcontractor_city** | **str** | City of the company the requisition is from | [optional] 
**subcontractor_state_code** | **str** | State code of the company the requisition is from | [optional] 
**subcontractor_zip** | **str** | Zip code of the company the requisition is from | [optional] 
**subcontractor_country_code** | **str** | Country code of the company the requisition is from | [optional] 
**application_number** | **str** | Invoice number | [optional] 
**contract_for** | **str** | The contract title | [optional] 
**contract_date** | **date** | Date the signed contract is received | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_requisitions_get200_response_inner_summary_text import RestV11RequisitionsGet200ResponseInnerSummaryText

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11RequisitionsGet200ResponseInnerSummaryText from a JSON string
rest_v11_requisitions_get200_response_inner_summary_text_instance = RestV11RequisitionsGet200ResponseInnerSummaryText.from_json(json)
# print the JSON string representation of the object
print(RestV11RequisitionsGet200ResponseInnerSummaryText.to_json())

# convert the object into a dict
rest_v11_requisitions_get200_response_inner_summary_text_dict = rest_v11_requisitions_get200_response_inner_summary_text_instance.to_dict()
# create an instance of RestV11RequisitionsGet200ResponseInnerSummaryText from a dict
rest_v11_requisitions_get200_response_inner_summary_text_from_dict = RestV11RequisitionsGet200ResponseInnerSummaryText.from_dict(rest_v11_requisitions_get200_response_inner_summary_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


