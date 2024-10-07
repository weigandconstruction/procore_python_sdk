# RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**requested_by_id** | **str** | Party ID of the user who requested the signature | [optional] 
**signatory** | [**InspectionItemSignatureCapturedBy**](InspectionItemSignatureCapturedBy.md) |  | [optional] 
**signature** | [**ChecklistSignature**](ChecklistSignature.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response_data_inner import RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner from a JSON string
rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response_data_inner_instance = RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner.to_json())

# convert the object into a dict
rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response_data_inner_dict = rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response_data_inner_instance.to_dict()
# create an instance of RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner from a dict
rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response_data_inner_from_dict = RestV20CompaniesCompanyIdProjectsProjectIdInspectionItemsItemIdSignatureRequestsGet200ResponseDataInner.from_dict(rest_v20_companies_company_id_projects_project_id_inspection_items_item_id_signature_requests_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


